fruit_calories = {
    'Apple' : 130,
    'Avocado' : 50,
    'Banana' : 96,
    'Cherry' : 50,
    'Grapes' : 69,
    'Kiwi' : 61,
    'Mango' : 60,
    'Orange' : 47,
    'Peach' : 39,
    'Watermelon' : 30,
    'Lime' : 20,
}

fruit = input("Фрукт: ")

if fruit in fruit_calories:
    calories = fruit_calories[fruit]
    print(f"Калории: {calories}")