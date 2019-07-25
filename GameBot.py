import telebot
import ResoursesGSB
import ChooseTypeOfResourses
import DBdirectioner

bot = telebot.TeleBot('Тут токен')
resourses = ResoursesGSB

""" 
    этот метот старта бота, можно написать чо угодно
"""

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


""" 
    это пин приказа
"""


@bot.message_handler(commands=['pin'])
def pinCommandInChates(message):
    chatsID = ['Тут айди чатов, где надо пинить приказы', 'и тут тоже', 'и так далее']
    admins = ['тут айди наших админов, которые могут отдавать приказы, чтобы простые смертные не имели такой привелегии']
    truePin = 0
    for i in admins:
        if message.chat.id == i:  # Проверяем, кто отправил приказ
            placeToAttack = message.text[message.text.find('n ') + 2:]  # достаем место куда надо идти
            messageToAttack = "Мои дорогие, все идем на: " + placeToAttack  # вот тут можно изменять сообщение которое будет пиниться
            truePin = 1

        if truePin == 1:
            for j in chatsID:  # Пробегаем по всем чатам и пиним там сообщения
                sendMessageVal = bot.send_message(j, messageToAttack)
                bot.pin_chat_message(j, sendMessageVal.message_id)
            else:
                bot.send_message(message.chat.id, 'У вас нет таких привелегий;(')


""" 
    Это парсер рюкзака
    пока не до-конца готов)
    надо будет разобраться с БД и я все сделаю по-человечески
"""

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if (message.forward_from.username == "@rf_telegram_bot"):
        DBdirectioner.create(message.text)




bot.polling() #Строчка обязательная
