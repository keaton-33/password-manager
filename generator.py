import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate():
    password = [random.choice(letters) for _ in range(16)]
    num_numbers = random.randint(3, 4)
    num_symbols = random.randint(3, 4)
    for i in range(0, num_numbers):
        numbers_generated = False
        while not numbers_generated:
            random_placement = random.randint(0, len(password) - 1)
            b = 0
            for n in numbers:
                if password[random_placement] != n:
                    b += 1
                    if b == len(numbers):
                        numbers_generated = True
                else:
                    break
        password[random_placement] = random.choice(numbers)

    for i in range(0, num_symbols):
        symbols_generated = False
        while not symbols_generated:
            random_placement = random.randint(0, len(password) - 1)
            b = 0
            c = 0
            for n in numbers:
                if password[random_placement] != n:
                    b += 1
                    if b == len(numbers):
                        for s in symbols:
                            if password[random_placement] != s:
                                c += 1
                                if c == len(symbols):
                                    symbols_generated = True
                else:
                    break
        password[random_placement] = random.choice(symbols)

    user_password = ''.join(password)
    return user_password
