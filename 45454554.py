
print("File: ")
with open("op.txt", 'r', encoding="utf-8") as f1:
    txt1 = f1.read()
    print(txt1)

print("Зашифровано: ")

import re
txt1 = txt1.replace("я","а")
txt1 = txt1.replace("б","а")
txt1 = txt1.replace("в","б")
txt1 = txt1.replace("г","в")
txt1 = txt1.replace("д","г")
txt1 = txt1.replace("е","д")
txt1 = txt1.replace("ё","е")
txt1 = txt1.replace("ж","ё")
txt1 = txt1.replace("з","ж")
txt1 = txt1.replace("и","з")
txt1 = txt1.replace("й","и")
txt1 = txt1.replace("к","й")
txt1 = txt1.replace("л","к")
txt1 = txt1.replace("м","л")
txt1 = txt1.replace("н","м")
txt1 = txt1.replace("о","н")
txt1 = txt1.replace("п","о")
txt1 = txt1.replace("р","п")
txt1 = txt1.replace("с","р")
txt1 = txt1.replace("т","с")
txt1 = txt1.replace("у","т")
txt1 = txt1.replace("ф","у")
txt1 = txt1.replace("х","ф")
txt1 = txt1.replace("ц","х")
txt1 = txt1.replace("ч","ц")
txt1 = txt1.replace("ш","ч")
txt1 = txt1.replace("щ","ш")
txt1 = txt1.replace("ъ","щ")
txt1 = txt1.replace("ы","ъ")
txt1 = txt1.replace("ь","ы")
txt1 = txt1.replace("э","ь")
txt1 = txt1.replace("ю","э")
txt1 = txt1.replace("а","я")

print(txt1)
print












