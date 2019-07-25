import DarkDB
import os.path


pathTodb = "db\\"  #путь, где будут лежать все файлы с инфой об игроках
textToWrite = "default"  #дополнительная переменная с которой работает программа
ddb = DarkDB


#метод, принимающий сообщение и изменяющий его для записи в файл
#вызывается при получении сообщения от игрока
def create(inputText):
    textToWrite = inputText

dicOfKeys = ["Экипировка", "Идентификатор"] #словарь выражений, чтобы определить что нам пристал игрок
for i in dicOfKeys:
    j = 0 #тип сообщения от игрока(инвентарь или информация о герое
    if textToWrite.includes(i): #если сообщение содержит регулярное выражение,
        outType = j  #выводим тип сообщения
        break
    else:
        j += 1 #иначе увеличиваем счетчик


#метод, который измененную строку записывает в файл
def direct(userID):

    if os.path.isfile(pathTodb + userID + ".ddb"): #если файл существует

       if outType == 0:

        ddb.update() # мы его обновляем


       elif outType == 1:


    else: #иначе мы создаем файл

        if outType == 0:

            ddb.create()

        elif outType == 1:


#метот меняющий строку, принимает тект и тип сообщения

def changeString(text, type):
    str = text
    tp = type

    if type == 0:
