class Assistant:
    def __init__(self):
        self.name = "Victor"
        self.version = "0.2"

    def reply(self, message):
        message = message.strip().lower()

        if message == "":
            return "Please type a message."

        if "hello" in message:
            return "Hello Sipho! I'm Victor. It's great to see you."

        if "how are you" in message:
            return "I'm operating perfectly and ready to help."

        if "who are you" in message:
            return "I'm Victor, your AI desktop assistant."

        return "I understand your message, but I haven't learned how to answer that yet."