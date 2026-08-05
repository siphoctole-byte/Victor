from tools.apps import AppTools
from ai.ollama_provider import OllamaProvider
from tools.system_tools import SystemTools


class Assistant:
    def __init__(self):
        self.ai = OllamaProvider()

    def reply(self, message):
        text = message.lower()

        # -----------------------------
        # Time and Date
        # -----------------------------
        if "time" in text and "date" in text:
            return (
                f"Today is {SystemTools.current_date()}.\n"
                f"The current time is {SystemTools.current_time()}."
            )

        if "time" in text:
            return f"The current time is {SystemTools.current_time()}."

        if "date" in text or "today" in text:
            return f"Today is {SystemTools.current_date()}."

        if "year" in text:
            return f"The current year is {SystemTools.current_year()}."

        # -----------------------------
        # Open Applications
        # -----------------------------
        if "open notepad" in text:
            return AppTools.open_notepad()

        if "open calculator" in text:
            return AppTools.open_calculator()

        # -----------------------------
        # AI Response
        # -----------------------------
        return self.ai.ask(message)