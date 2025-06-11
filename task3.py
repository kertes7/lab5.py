import random

code = random.randint(1, 20)
attempts = 3

while attempts > 0:
    try:
        guess = int(input("Введіть число від 1 до 20: "))
        if guess == code:
            print("Вітаємо! Ви вгадали код.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Невірно. Залишилось спроб: {attempts}")
            else:
                print(f"Ви програли. Правильний код був: {code}")
    except ValueError:
        print("Це не число.")
