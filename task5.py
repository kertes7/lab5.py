import tkinter as tk
import random

colors = ['червоний', 'синій', 'зелений', 'жовтий', 'фіолетовий']
warm = ['червоний', 'жовтий']
cold = ['синій', 'зелений', 'фіолетовий']
secret_color = random.choice(colors)
attempts = 3

def check_guess():
    global attempts
    guess = entry.get().strip().lower()
    
    if guess == secret_color:
        result_label.config(text="Вітаємо! Ви вгадали колір!", fg="green")
        button.config(state="disabled")
    elif guess in colors:
        attempts -= 1
        hint = "теплих" if secret_color in warm else "холодних"
        if attempts > 0:
            result_label.config(
                text=f"Невірно. Колір належить до {hint}. Залишилось спроб: {attempts}",
                fg="orange"
            )
        else:
            result_label.config(
                text=f"Ви не вгадали. Загаданий колір був: {secret_color}",
                fg="red"
            )
            button.config(state="disabled")
    else:
        result_label.config(text="Такого кольору немає в списку.", fg="blue")

root = tk.Tk()
root.title("Кольоровий код — Гра")
root.geometry("400x250")

tk.Label(root, text="Вгадайте колір:", font=("Arial", 14)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack()

button = tk.Button(root, text="Перевірити", command=check_guess, font=("Arial", 12))
button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

tk.Label(root, text="Список кольорів:\nчервоний, синій, зелений, жовтий, фіолетовий", font=("Arial", 10)).pack()

root.mainloop()
