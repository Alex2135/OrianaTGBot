import random

answers = {
    1: ["Здравствуй, меня зовут Ориана",
                "Приветствую тебя, призыватель",
                "Привет, давай знакомиться, я умный бот Ориана",
                "Привет, чем могу помочь?"]
    ,2: ["Комманды:\nпривет\nмемчики\nне мемчики\nфото всратого попугая"]
    ,3: ["Сам говно!"]
}
requests = {
    1: ["привет", "здравствуй", "хай", "здарова"]
    ,2: ["help", "помощь", "команды"]
    ,3: ["говно"]
}
noanswer = [
    "Таких комманд не знаю!",
    "Не нервируй меня!",
    "Напиши что-нибудь нормальное нормально!",
    "Шар в гневе!",
    "Чем больше я узнаю людей, тем больше люблю свой шар..."
]

class BotAnswers:
    def __init__(self, _request_words):
        self.request_words = _request_words

    def get_request_key(self, _word):
        for key, key_words in requests.items() :
            if _word in key_words :
                return key
        return False

    def get_answer(self):
        answer = ""

        size = len( self.request_words )
        # 3 - 0,1,2 ; 7 - 0,1,2,3,4,5,6
        for i in range( size ): # 0,1,2,3,4, ... ,size-1
            word = self.request_words[ i ]
            key = self.get_request_key(word)
            if key != False:
                current_answers = answers[key]
                answer = random.choice( current_answers )
                break
            else:
                answer = random.choice( noanswer )


        return answer
