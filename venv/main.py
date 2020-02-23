import requests
import random
#import UserRequest
from UserRequest import UserRequest

token = "828701322:AAHmypcH0GN-LkATiPZfHx9lv9kzFk4kZ5Y"
url = "https://api.telegram.org/bot" + token + "/"

print( token )
print( url + "getMe" )
# javasript object notation

def last_update( request ):
    # Получение ответа на запрос по URL
    response = requests.get( request + "getUpdates" )
    response = response.json()

    results = response["result"]

    # число, номер последнего єл-то в массиве results
    total_updates = len(results) - 1
    return results[ total_updates ]

def get_chat_id( update ) :
    chat_id = update["message"]["chat"]["id"]
    return chat_id

def get_message_text( update ) :
    message_text = update["message"]["text"]
    return message_text

def send_message( chat, text ):
    params = { "chat_id" : chat, "text": text }

    response = requests.post(url + "sendMessage", data = params)
    return response

def send_photo( chat_id, photo_url ):
    params = { "chat_id" : chat_id, "photo" : photo_url }
    response = requests.post( url + "sendPhoto", data = params )
    return response

meme_urls = [
    "https://cutt.ly/br0oNmN",
    "https://i.imgur.com/OhX2e2N.jpg",
    "https://i.pinimg.com/originals/10/12/f7/1012f7bb91d4e651992715ae5864b4ff.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQvUm2uo3Ql27P1Tdpghlpu5Ldh49oITMvhK1kOgQ0KehNrrhSe"
]

riot_api = 'RGAPI-62c8eb88-7e15-4e5a-a838-24ff0e6af449'
host = "https://ru.api.riotgames.com"

def main():
    update_id = last_update( url )["update_id"] # 3

    while True :
        update = last_update( url ) # 3

        if update_id == update["update_id"] :
            # "ABC", "abc"
            message = get_message_text( update ).lower()
            chat_id = get_chat_id( update )

            if  message == "мемчики":
                index = random.randint( 0, len(meme_urls) - 1)
                random_photo = meme_urls[ index ]
                resp = send_photo(chat_id, random_photo)
            elif message == "фото всратого попугая" :
                send_photo(chat_id, meme_urls[0])
            else:
                userrequest_obj = UserRequest(message)
                answer = userrequest_obj.get_answer()
                if answer:
                    send_message(chat_id, answer)

            update_id += 1

main()
