from datetime import datetime


class SystemTools:

    @staticmethod
    def current_time():
        return datetime.now().strftime("%H:%M")

    @staticmethod
    def current_date():
        return datetime.now().strftime("%A, %d %B %Y")

    @staticmethod
    def current_year():
        return str(datetime.now().year)