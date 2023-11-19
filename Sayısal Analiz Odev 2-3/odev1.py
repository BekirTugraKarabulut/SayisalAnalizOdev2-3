a = 0
xilk = 2
xson = 4

print("---2. Ödev a) Sorusu---\n")

for i in range(0,4):

    fonksiyon = a * a * a  - 2 * a * a - 5

    a = (xilk + xson) / 2

    xkok = a

    if(fonksiyon > 0):
        xilk = a

    else:
        xson = a

    print("Kökleri : " , a)            