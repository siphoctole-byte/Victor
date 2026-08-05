from ollama import chat


class OllamaProvider:
    def __init__(self, model="llama3.2:3b"):
        self.model = model

    def ask(self, prompt: str) -> str:
        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]