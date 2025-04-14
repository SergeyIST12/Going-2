slovar = {"0": "ноль", '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', 
          '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}

def Ermolaev(text):
    num = []
    with open(text, "r") as file:
        while (line := file.readline().strip()):  # Читаем файл построчно
            for a in line.split():
                if all(c in "01" for c in a) and len(a) > 1 and a[-2:] == "00":
                    dec = int(a, 2)
                    if dec <= 2047 and dec % 2 == 0:
                        num.append(dec)

    if num:
        for n in num:
            print("".join(c for c in str(n) if c != "0") or "0")
        avg = (min(num) + max(num)) // 2
        print(" ".join(slovar[d] for d in str(avg)))

Ermolaev("1.txt")
