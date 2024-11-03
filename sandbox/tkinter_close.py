import tkinter as tk
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()  # ユーザーが「OK」をクリックした場合、ウィンドウを閉じる

root = tk.Tk()
root.title("Tkinter Example")

# 閉じるボタンがクリックされたときの処理をバインド
root.protocol("WM_DELETE_WINDOW", on_closing)

# ウィンドウのサイズやコンテンツを設定
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

root.mainloop()
