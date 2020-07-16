# 4) Напишите функцию который будет конвертировать Фаренгейт в Цельсии и
# наоборот.
def fah2cel(fah):
    if 'cel'in string:
        cel_result = 5.0*(fah - 32) / 9
        print(cel_result)
    elif 'fah' in string:
        fah_result = (9 / 5.0 * fah) + 32
        print(fah_result)
string=(input("чтобы ввывести  фаренгейт 'fah'цельции 'cel': "))
b =float(input("введите градус: "))
fah2cel(b)
