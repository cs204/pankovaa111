months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

while True:
    date = input("Дата: ")
    if "." in date:
        parts = date.split(".")
    else:
        parts = date.split(" ")
    if len(parts) != 3:

        continue
    day_string = parts[0]
    month_string = parts[1].lower()
    year_string = parts[2]

    try:
        day = int(day_string)
        year = int(year_string)
    except ValueError:

        continue

    if month_string not in months:
        try:
            month = int(month_string)
            if month < 1 or month > 12:
                print("Неправильный формат даты")
                continue
        except ValueError:
            print("Неправильный формат даты")
            continue
    else:
        month = months.index(month_string) + 1

    if len(str(year)) != 4:
        print("Неправильный формат даты")
        continue

    print(f"{year}-{month:02d}-{day:02d}")
    break