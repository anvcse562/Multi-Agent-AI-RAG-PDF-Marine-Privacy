import requests

class GroqEmbedder:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = "https://api.groq.com/v1/embeddings"  # replace with the correct Groq API URL

    def get_embedding(self, text):
        # Assuming Groq uses a POST request to get embeddings
        response = requests.post(
            self.endpoint,
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"text": text}
        )
        response.raise_for_status()
        return response.json()['embedding']  # Adjust this based on the actual API response format