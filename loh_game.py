
import pygame

# Инициализация Pygame
pygame.init()

# Устанавливаем иконку
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

import tkinter as tk
from PIL import Image, ImageTk
import random

# Список людей и их фото
people = {
    "Амир": "amir.png",
    "Нарбек": "narbek.png",
    "Джалиль": "jalil.png"
}

spinning = False  # Флаг вращения
chosen_label = None  # Выбранный "лох"

# Функция обновления положения фото
def update_positions():
    if spinning:
        positions = [
            (150, 250),
            (250, 150),
            (350, 250)
        ]
        random.shuffle(positions)  # Меняем местами фото

        for i, label in enumerate(photo_labels):
            label.place(x=positions[i][0], y=positions[i][1])

        root.after(100, update_positions)  # Запускаем снова
    else:
        choose_loh()  # Определяем "лоха"

# Функция плавного поднятия победителя
def move_winner(y):
    if y > 50:
        chosen_label.place(x=250, y=y)
        root.after(30, move_winner, y - 10)
    else:
        result_label.place(x=180, y=y + 120)  # Показываем надпись ниже фото

# Функция выбора "лоха"
def choose_loh():
    global chosen_label
    chosen_index = random.randint(0, 2)
    chosen_label = photo_labels[chosen_index]

    # Убираем другие фото
    for i, label in enumerate(photo_labels):
        if i != chosen_index:
            label.place_forget()

    # Запускаем плавное поднятие
    move_winner(250)

    # Показываем текст
    result_label.config(text="Лошара, сгоняй за пивом!", fg="red", font=("Arial", 20, "bold"))

# Функция запуска кручения
def start_spinning():
    global spinning
    spinning = True
    result_label.config(text="Крутим...", fg="white")
    result_label.place_forget()  # Скрываем текст в начале
    update_positions()
    root.after(3000, stop_spinning)  # Крутим 3 секунды

# Функция остановки вращения
def stop_spinning():
    global spinning
    spinning = False  # Останавливаем кручение

# Создаём окно
root = tk.Tk()
root.title("Кто ЛОХ? 🤡")
root.geometry("600x500")
root.configure(bg="#2E2E2E")

# Загружаем фото людей
people_images = {name: ImageTk.PhotoImage(Image.open(file).resize((100, 100))) for name, file in people.items()}

# Загружаем картинку пива
beer_img = ImageTk.PhotoImage(Image.open("beer.png").resize((150, 200)))
beer_label = tk.Label(root, image=beer_img, bg="#2E2E2E")
beer_label.place(x=225, y=300)  # Ставим пиво в центр

# Размещаем 3 изображения (изначально случайные позиции)
photo_labels = []
for i, name in enumerate(people.keys()):
    lbl = tk.Label(root, image=people_images[name], bg="#2E2E2E")
    lbl.place(x=150 + i * 100, y=250)
    photo_labels.append(lbl)

# Кнопка старта
spin_button = tk.Button(root, text="Кто ЛОХ?", font=("Arial", 18), command=start_spinning, bg="#FFD700", fg="black", padx=20, pady=10)
spin_button.pack(pady=20)

# Текст с результатом (изначально скрыт)
result_label = tk.Label(root, text="", font=("Arial", 20), fg="white", bg="#2E2E2E")
result_label.place(x=180, y=180)  # Расположен ниже фото

# Запуск окна
root.mainloop()