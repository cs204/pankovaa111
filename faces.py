def convert(text) :
    text = text.replace(':)', '\U0001F642')
    text = text.replace(':(', '\U0001F641')
    return text
def main():
    user_input = input()
    result = convert(user_input)
    print(result)
main ()