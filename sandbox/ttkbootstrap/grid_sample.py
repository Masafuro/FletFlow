import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window()

# 1行目の3列を1つに結合したラベル
label1 = ttk.Label(root, text="1行目 - 3列を結合")
label1.grid(row=0, column=0, columnspan=3, sticky=N, padx=5, pady=5)

# 2行目と3行目のウィジェット（個別のセル）
button1 = ttk.Button(root, text="Button (2, 1)")
button1.grid(row=1, column=0, padx=5, pady=5)

button2 = ttk.Button(root, text="Button (2, 2)")
button2.grid(row=1, column=1, padx=5, pady=5)

button3 = ttk.Button(root, text="Button (2, 3)")
button3.grid(row=1, column=2, padx=5, pady=5)

button4 = ttk.Button(root, text="Button (3, 1)")
button4.grid(row=2, column=0, padx=5, pady=5)

button5 = ttk.Button(root, text="Button (3, 2)")
button5.grid(row=2, column=1, padx=5, pady=5)

button6 = ttk.Button(root, text="Button (3, 3)")
button6.grid(row=2, column=2, padx=5, pady=5)

# ウィンドウのリサイズに応じて全セルが伸縮するように設定
for i in range(3):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
