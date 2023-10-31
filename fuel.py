while True:
    try:
        fraction = input("Дробь: ").strip()
        if '/' not in fraction:
            raise ValueError
        x, y = fraction.split('/')
        if not x.isdigit() or not y.isdigit():
            raise ValueError
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        percentage = round(x / y * 100)
        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")
        break
    except ValueError:
        print("Некорректный ввод. Введите дробь в формате x/y, где x и y - целые числа.")
    except ZeroDivisionError:
        print("Некорректный ввод. Знаменатель не может быть равен нулю.")