#coding=utf-8
import random
import tkinter as tk
import time
from tkinter import messagebox

def center_window(window, width, height):
    # 获取屏幕尺寸
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 计算窗口的宽度和高度
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # 设置窗口的位置
    window.geometry(f'{width}x{height}+{x}+{y}')

# 设置窗口大小
window_width = 250
window_height = 300
# 窗口配置
window = tk.Tk()
window.title("Made By AB")
center_window(window, window_width, window_height)

# 保存名字变量
with open("name.txt") as f:
    name_list = f.readlines()

# 配置文件系统
with open('config.txt', 'r', encoding='gbk') as file:
    for line in file:
        if 'repeat_extraction' in line:
            key, value = line.strip().split('=')
            repeat_extraction = value.strip()
            break

with open('config.txt', 'r', encoding='gbk') as file:
    for line in file:
        if 'extractions_number' in line:
            key, value = line.strip().split('=')
            extractions_number = int(value.strip())
            break

# 触发逻辑(重复抽取)
history = []

def button_click():
    if repeat_extraction == 'true':
        for i in range(30):
            Label.config(text=random.choice(name_list))
            window.update()
            time.sleep(0.05)
        if Label.cget('text') in history:
            for i in range(extractions_number):
                Label.config(text=random.choice(name_list))
                window.update()
                time.sleep(0.05)
        history.append(Label['text'])

    else:
        for i in range(extractions_number):
            Label.config(text=random.choice(name_list))
            window.update()
            time.sleep(0.05)

# 控件
Label = tk.Label(window, text="点击抽取👇", font=("Microsoft YaHei", 30))
Label.place(x=25, y=70, width=200, height=100)

button = tk.Button(window, text="换一个", font=("Microsoft YaHei", 20), command=button_click)
button.config(bg="#00C12D")
button.place(x=50, y=180, width=150, height=80)

# 消息弹窗
messagebox.showinfo("当前配置", "是否重复抽取：{}".format(repeat_extraction), )

window.mainloop()