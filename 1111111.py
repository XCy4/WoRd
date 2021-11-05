print("File: ")
with open("op.txt", 'r', encoding="utf-8") as f:
    txt = f.read()
    txt = txt.split('\n')
    txt = [str[2:] for str in txt]
    print(txt)




print('File1: ')
with open("op1.txt", 'r', encoding="utf-8") as f1:
    txt1 = f1.read()
    txt1 = txt1.split('\n')
    txt1 = [str[2:] for str in txt1]
    print(txt1)
print('Result: ')
c = []
for i in txt:
    print(i)
    if i in c:
        continue
    for j in txt1:
        if i == j:
            c.append(i)
            break


print(c)
