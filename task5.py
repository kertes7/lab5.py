import random

colors = ['червоний', 'синій', 'зелений', 'жовтий', 'фіолетовий']
warm = ['червоний', 'жовтий']
cold = ['синій', 'зелений', 'фіолетовий']
secret_color = random.choice(colors)
attempts = 3

while attempts > 0:
    guess = input("Вгадайте колір: ").strip().lower()
    if guess == secret_color:
        print("Вітаю! Ви вгадали колір.")
        break
    elif guess in colors:
        attempts -= 1
        group = "теплих" if secret_color in warm else "холодних"
        print(f"Ні, але колір з групи {group}. Залишилось спроб: {attempts}")
    else:
        print("Немає такого кольору в списку.")
