import ollama

class Llama:
    def __init__(self, host:str, model_name:str):
        self.host = host
        self.client = ollama.Client(host=self.host)
        self.model_name = model_name

    def ModelInfo(self):
        print(f"Connecting to {self.host}...")
        print(f"Checking for {self.model_name} (It will download automatically if missing)...")


    def Inference(self):
        # Connect to Ollama using the environment variable set by Docker Compose
        # This safely pulls the model if it doesn't exist yet!
        self.client.pull(self.model_name)

        print("\nSending prompt to Llama 3.2...")
        response = self.client.chat(model=self.model_name, messages=[
            {'role': 'user', 'content': 'Explain apple in one short sentence.'}
            ])

        print("\n--- Llama 3.2 Response ---")
        print(response['message']['content'])