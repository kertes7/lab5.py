import random

pin = str(random.randint(1000, 9999))
attempts = 5

while attempts > 0:
    guess = input("Введіть 4-значний PIN-код: ")
    if guess == pin:
        print("Вітаю! Ви вгадали PIN-код.")
        break
    elif len(guess) == 4 and guess.isdigit():
        correct = sum(1 for i in range(4) if guess[i] == pin[i])
        attempts -= 1
        if attempts > 0:
            print(f"Правильних цифр на місці: {correct}. Залишилось спроб: {attempts}")
        else:
            print(f"Спроби закінчились. PIN-код був: {pin}")
    else:
        print("Введіть саме 4 цифри.")
