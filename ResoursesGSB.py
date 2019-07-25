


def work(inputText, PlayerID):

    outValue = gold(inputText)
    file = open(PlayerID + '.txt', 'w')
    file.write()
    outValue = silver(inputText)
    outValue = bronze(inputText)







def gold(inputTextGold):
    j = inputTextGold
    x = j.find('Золотой слиток')
    y = j.find(')')
    g = j[x:y]
    x = g.find('(')
    g = g[x:]
    return g

def silver(inputTextSilver):
    j = inputTextSilver
    x = j.find('Серебряный слиток')
    y = j.find(')')
    s = j[x:y]
    x = s.find('(')
    s = s[x+1:]
    return s

def bronze(inputTextBronze):
    j = inputTextBronze
    x = j.find('Бронзовый слиток')
    y = j.find(')')
    s = j[x:y]
    x = s.find('(')
    s = s[x+1:]
    return s





