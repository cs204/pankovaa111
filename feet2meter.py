def main ():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(str):
 str=str .strip('ft')
 result = float(str)
 result = result * 0.3048
 return result
main ()