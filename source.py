import ollama
import os
import time

from comments import Comments # source code, then class name
from llama import Llama       # source code, then class name

def main():
    ## start
    start = time.time()
    msg = Comments('Calculation started.', 'Calculation completed.')        
    msg.begin()    
    ##

    lm = Llama(os.environ.get('OLLAMA_HOST', 'http://localhost:11434'), 'llama3.2:1b')
    lm.ModelInfo()
    lm.Inference()

    ## end
    msg.end()                      # message method
    end = time.time() # time display
    print(f"### elapsed_time: {end - start:.2f} [sec] ###")
    ##

# --- main routine ---
if __name__ == '__main__':
    main()

## run the below
# Start your stack in the background: docker compose up -d
# "get inside" by opening a bash shell: docker exec -it my-llama-app bash
# docker exec -it llama-app python3 source.py
# Namely...
# 1. docker compose up -d
# 2. docker exec -it llama-app python3 source.py

## build command
# docker compose up -d --build