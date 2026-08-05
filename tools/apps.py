import subprocess
import platform


class AppTools:

    @staticmethod
    def open_notepad():
        if platform.system() == "Windows":
            subprocess.Popen("notepad")
            return "Opening Notepad."

        return "Notepad is only supported on Windows."

    @staticmethod
    def open_calculator():
        if platform.system() == "Windows":
            subprocess.Popen("calc")
            return "Opening Calculator."

        return "Calculator is only supported on Windows."