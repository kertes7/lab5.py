import random

def limited_attempts_code():
    secret = random.randint(1, 20)
    attempts = 3
    while attempts > 0:
        print(f"Очікується введення... (залишилось {attempts} спроб)")
        guess = input(f"Вгадайте число від 1 до 20: ")  
        if not guess.isdigit(): 
            print("Будь ласка, введіть число!")
            continue  
        
        guess = int(guess)  
        if guess == secret:
            print("Вітаю, ви вгадали!")
            return
        attempts -= 1
    
    print(f"Ви програли! Загадане число: {secret}")

limited_attempts_code()
