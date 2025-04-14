import re

slovar = {
    "0": "ноль", '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
    '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
}

def Ermolaev(text):
    num = []
    # Регулярка: чётные двоичные числа длиной до 11 символов, с 0 на втором месте справа
    pattern = re.compile(r'\b[01]{2,11}0\b(?<=0.0\b)')

    with open(text, "r") as file:
        content = file.read()
        for a in pattern.findall(content):
            dec = int(a, 2)
            if dec <= 2047:  # только эта проверка остаётся вне регулярки
                num.append(dec)

    if num:
        for n in num:
            print("".join(c for c in str(n) if c != "0") or "0")
        avg = (min(num) + max(num)) // 2
        print(" ".join(slovar[d] for d in str(avg)))
    else:
        print("Подходящих чисел не найдено")

Ermolaev("1.txt")
