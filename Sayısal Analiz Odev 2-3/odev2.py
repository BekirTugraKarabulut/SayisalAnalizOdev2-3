a = 0
xilk = 1
xson = 2

print("---2. Ödev b) Sorusu---\n")

for i in range(0,4):

    fonksiyon = a * a * a  + 4 * a * a - 10

    a = (xilk + xson) / 2

    xkok = a

    if(fonksiyon > 0):
        xilk = a

    else:
        xson = a

    print("Kökleri : " , a)            