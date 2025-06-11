import random

secret = random.randint(1, 50)

while True:
    try:
        guess = int(input("Вгадай число від 1 до 50: "))
        diff = abs(secret - guess)

        if guess == secret:
            print("Вітаю! Ви вгадали число.")
            break
        elif diff <= 3:
            print("Дуже близько!")
        elif diff <= 10:
            print("Близько.")
        else:
            print("Далеко.")
    except ValueError:
        print("Будь ласка, введіть ціле число.")
