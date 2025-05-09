# Créé par doyen, le 06/03/2025 en Python 3.7
def convert_to_x_base(base, number):
    try:
        if base > 10 or base < 2:
            print("This programmes handles bases between 2 and 10.")
        else:
            origin_number = number
            modules_list = []

            while number > 0:
                module = number % base
                modules_list.insert(0, round(module))
                number = (number - module) / base
            print(f"Base 10 : {origin_number}")
            print(f"Base {base} : {''.join(map(str, modules_list))}")
    except ValueError:
        print("Choose a NUMBER, not a string.")
    except KeyboardInterrupt:
        print("Have you never been taught to say goodbye politely ?")


while True:
    base = int(input("Which base number are you choosing ?"))
    number = int(input("Which number do you want to convert ?"))
    convert_to_x_base(base, number)