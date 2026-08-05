from ai.ollama_provider import OllamaProvider

victor = OllamaProvider()

print("Victor is thinking...\n")

reply = victor.ask("Who are you? Answer in one sentence.")

print(reply)