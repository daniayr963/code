import tkinter as tk
import sqlite3
import random

# Создаем окно приложения
app = tk.Tk()
app.title("Random Joke App")

# Создаем виджет Text для вывода анекдотов
joke_text = tk.Text(app, width=40, height=10)
joke_text.pack()

# Функция для вывода случайного анекдота
def jokes():
    connection = sqlite3.connect('jokes.db')
    cursor = connection.cursor()
    cursor.execute("SELECT joke FROM Jokes ORDER BY RANDOM() LIMIT 1")
    joke = cursor.fetchone()
    connection.close()
    
    if joke:
        joke_text.delete(1.0, tk.END)  # Очищаем текстовое поле
        joke_text.insert(tk.END, joke[0])  # Вставляем случайный анекдот

# Создаем кнопку для получения случайного анекдота
get_joke_button = tk.Button(app, text="Получить анекдот", command=get_random_joke)
get_joke_button.pack()

app.mainloop()