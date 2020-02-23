from BotAnswers import BotAnswers

class UserRequest:
    # self - ссылка на объект, который мы создали
    # def - definitoin - определение функции
    def __init__(self, _request):
        self.request = _request.lower()

    def clean_request(self):
        result = ""

        for char in self.request :
            if not (not char.isalpha() and not char.isnumeric() and char != " "):
                result += char

        return result

    def get_answer(self):
        clear_request = self.clean_request()
        request_words = clear_request.split(" ")
        if type(request_words) == list :
            if "" in request_words:
                request_words.remove("")
        else:
            request_words = [request_words]
        bot = BotAnswers( request_words )
        answer = bot.get_answer()

        return answer
