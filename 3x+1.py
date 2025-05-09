number = 0

while True:
    number += 1
    copy_number = number
    steps = 0

    while copy_number != 1:
        if copy_number % 2 == 0:
            copy_number = copy_number / 2
        else:
            copy_number = copy_number * 3 + 1
        steps += 1

    print(f"{number} works ({steps} steps)")