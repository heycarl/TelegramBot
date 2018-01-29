import telebot
import constants
import urllib.request as urllib2
import os
import requests
from bs4 import BeautifulSoup
feedback = "Отзыв"
bot = telebot.TeleBot(constants.token)
urls = ["dollar", "euro", "rubl", "zloty"]
url = "https://finance.tut.by/kurs/minsk/"



def log(message, answer):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст = {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id), message.text))
    print(answer)

def log2(message, answer2):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Отзыв от {0} {1}. (id = {2}) \n Текст = {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id), message.text))


@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('/start', '/feedback', '/stop', '/kurs')
    user_markup.row('фото', 'аудио', 'документы', 'евро')
    user_markup.row('стикер', 'видео', 'голос', 'локация')
    bot.send_message(message.from_user.id, 'Добро пожаловать...', reply_markup=user_markup)
    answer = "Клавиатура показана"
    log(message, answer)

@bot.message_handler(commands=['feedback'])
def handle_text(message):
    user_markup2 = telebot.types.ReplyKeyboardMarkup(True)
    user_markup2.row('/Да', '/Нет')
    bot.send_message(message.from_user.id, 'Хочешь оставить отзыв,', reply_markup=user_markup2)
    answer = "Пользователь оставил отзыв"
    log(message, answer)

@bot.message_handler(commands=['kurs'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    bot.send_message(message.from_user.id, 'Вот курсы валют на сегодня:', reply_markup=user_markup)
    answer = "Пользователь получил курс"
    i = 0
    while i < len(urls):
        this_url = url + urls[i]
        r = requests.get(this_url)
        r = r.text
        r = r.encode("utf-8")
        f = open('index.html', 'wb').write(r)
        soup = BeautifulSoup(r, 'html.parser')
        find_kurs = soup.find('b', class_="red")
        find_kurs = find_kurs.text
        answer = urls[i] + ": " + find_kurs
        i += 1
        bot.send_message(message.chat.id, answer)
        log(message, answer)

@bot.message_handler(commands=['Да'])
def handle_start(message):
    hide_markup2 = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "Спасибо! Напиши свой отзыв в следующем сообщении и все!", reply_markup=hide_markup2)
    answer = "Убрана клавиатура2"
    log(message, answer)
    constants.feb = True


@bot.message_handler(commands=['Нет'])
def handle_start(message):
    hide_markup2 = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "Ок, может, потом захочешь))", reply_markup=hide_markup2)
    answer = "Убрана клавиатура2"
    log(message, answer)
    constants.feb = False

@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "...", reply_markup=hide_markup)
    answer = "Убрана клавиатура"
    log(message, answer)

@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, """Привет! Я робот которого создал мальчик Саша. Я нужен в основном для веселья. Ты можешь высказать свои предложения, если выберешь вкладку /feedback. Функций пока мало, но ты только посмотри! Все работает!!!""")
    answer = "Хелп написаный Сашей"
    log(message, answer)
    print(bot.get_me())

@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = "Слажна, непонятно!"

    if message.text == "а":
        answer = "Б"
        log(message, answer)
        bot.send_message(message.chat.id, "Б")

    elif message.text == "б":
        answer = "В"
        bot.send_message(message.chat.id, "В")
        log(message, answer)

    elif message.text == "1" or message.text == "2":
        bot.send_message(message.chat.id,  "Ну, это или 1 или 2 ).... ")

    elif message.text == "?" and str(message.from_user.id) == "321965003":
        bot.send_message(message.chat.id, "Ты ибранный, Нео.")

    elif message.text == 'фото':
        url = 'https://pp.userapi.com/c636216/v636216706/3301c/3PDy6wA37_g.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
        answer = "фото по ссылке"
        log(message, answer)

    elif message.text == 'евро':
        url2 = 'https://pp.userapi.com/c837638/v837638171/3a414/NI_fSZBOI6U.jpg'
        urllib2.urlretrieve(url2, 'url_image2.jpg')
        img2 = open('url_image2.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img2)
        img2.close()
        answer = "фото с евро по ссылке"
        log(message, answer)

    elif message.text == 'аудио':
        audio = open("B:\Bots\Audio\lol.mp3", 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()
        answer = "аудиофайл с копьютера"
        log(message, answer)

    elif message.text == 'документы':
        directory = 'B:\Bots\Docs'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            document = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()
        answer = "документ с компьютера"
        log(message, answer)

    elif message.text == 'Что такое ардуино?':
        bot.send_message(message.chat.id, "Афигенная штука, которой пользуется всемогущий Саня")
        answer = "Афигенная штука, которой пользуется всемогущий Саня"
        log(message, answer)

    elif message.text == 'стикер':
        bot.send_sticker(message.chat.id, constants.template_sticker_id)
        answer = "стикер по id в файле с константами"
        log(message, answer)

    elif message.text == 'видео':
        video = open("B:\Bots\Video\kek.mp4", 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_video')
        bot.send_video(message.from_user.id, video)
        video.close()
        answer = "видео с компьютера"
        log(message, answer)

    elif message.text == 'голос':
        voice = open("B:\Bots\Voice\kek.ogg", 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_voice(message.from_user.id, voice)
        voice.close()
        answer = "аудио с компьютера для быстрого прослушивания"
        log(message, answer)

    elif message.text == 'локация':
        bot.send_chat_action(message.from_user.id, 'find_location')
        bot.send_location(message.chat.id, 53.124295, 23.892016)
        answer = "заданные координаты"
        log(message, answer)


    elif message.text == "Привет":
            bot.send_message(message.chat.id, "Привет! Чтобы начать мной пользоваться, нажми /start т.к. я понимаю не все команды")
            answer = "Ответ на привет"
            log(message, answer)

    elif message.text == "Как дела?":
            bot.send_message(message.chat.id, "Отлично! Ведь со мной общаешься ты, всемогущий человек")
            answer = "Ответ на Как дела?"
            log(message, answer)


    elif constants.feb == True:
        answer2 = "Отзыв пользователя"
        feedback = message.text
        answer2 = feedback
        log2(message, answer2)
        constants.feb = False

    else:
        bot.send_message(message.chat.id, "Слажна, непонятно!")
        answer = "Слажна, непонятно!"
        log(message, answer)






bot.polling(none_stop=True, interval=0)