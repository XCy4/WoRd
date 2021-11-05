import re
print('Text: ')
with open("dunduri.txt", 'r', encoding="utf-8") as f:
    txt = f.read()
    txt = txt.replace('\n', ' ')
    print(txt)





print(' ')
print(':LogList:')
txt = txt.split()
print(txt)
print(' ')
print('Кол-во слов: ') # Перед точкой или другим символом поставить пробел (Например: "убит.Сначала", СЧИТАЕТСЯ КАК ОДНО СЛОВО )
txt = len(txt)
print(txt)



