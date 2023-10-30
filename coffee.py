def main():
    amount_due = 50
    change_owed = 0

    print(f"Нужная сумма: {amount_due}")
    while change_owed < amount_due:
     coin = int(input("Вставьте монету: "))
     if coin in [50, 20, 10, 5]:
         change_owed += coin
         print(f"Ваша сдача: {amount_due - change_owed}")
     if change_owed > amount_due:
         print(f"Ваша сдача: {change_owed - amount_due}")
main()