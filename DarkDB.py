
#путь, где будут лежать все файлы с инфой об игроках
pathTodb = "db\\"

#создает новый файл
#принимает ID игрока и сообщение
#сообщение создается в файле DBdirection

def create(userID, inputString):
    pathToFile = pathTodb + userID + ".ddb"
    strToWrite = inputString

    file = open(pathToFile, 'w')
    file.write(strToWrite)
    file.close()

#изменяет созданый файл
#принимает ID игрока, ключ и значение

def update(userID, key, value):
    pathToFile = pathTodb + userID + ".ddb"

    file = open(pathToFile)
    firstInf = file.read()
    file.close()

    file = open(pathToFile, 'w')
    secondInf = firstInf[firstInf.find(key):firstInf.find("\n")]
    keyInFile = secondInf[0:secondInf.find(":")+1]
    outValue = keyInFile + " " + value
    firstInf = firstInf.replace(secondInf, outValue)
    file.write(firstInf)
    file.close()

#удаляет файл
#принимает ID игрока

def delete(userID):
    pathToFile = pathTodb + userID + ".ddb"
    file = open(pathToFile, 'w')
    file.close()

#пока не работает

def getInfo():
    print("get info\n")

