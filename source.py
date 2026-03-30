import ollama
import os

# Connect to Ollama using the environment variable set by Docker Compose
host = os.environ.get('OLLAMA_HOST', 'http://localhost:11434')
client = ollama.Client(host=host)

model_name = 'llama3.2:1b'

print(f"Connecting to {host}...")
print(f"Checking for {model_name} (It will download automatically if missing)...")

# This safely pulls the model if it doesn't exist yet!
client.pull(model_name)

print("\nSending prompt to Llama 3.2...")
response = client.chat(model=model_name, messages=[
    {'role': 'user', 'content': 'Explain Docker Compose in one short sentence.'}
])

print("\n--- Llama 3.2 Response ---")
print(response['message']['content'])

## run the below
# Start your stack in the background: docker compose up -d
# "get inside" by opening a bash shell: docker exec -it my-llama-app bash
# docker exec -it llama-app python3 source.py
# Namely...
# 1. docker compose up -d
# 2. docker exec -it llama-app python3 source.py

## build command
# docker compose up -d --build