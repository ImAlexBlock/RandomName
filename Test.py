import random
import tkinter as tk
import time
from plyer import notification

window = tk.Tk()
window.title("Random Name")
window.geometry("300x150")

with open("name.txt") as f:
    name_list = f.readlines()

def button_click():
    for i in range(30):
        Label.config(text=random.choice(name_list))
        window.update()
        time.sleep(0.05)

    notification.notify(
        title='Success',
        message='随机到幸运观众：'+ Label.cget("text"),
        timeout=1
    )

Label = tk.Label(window, text=random.choice(name_list), font=("Microsoft YaHei", 30))
Label.pack()

button = tk.Button(window, text="换一个", font=("Microsoft YaHei", 20), command=button_click)
button.pack()

window.mainloop()