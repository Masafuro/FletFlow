import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window()

# グリッドのサイズ設定
cell_size = 100  # 各セルのサイズ（ピクセル）
grid_size = 3    # グリッドの行・列の数

# ウィンドウのサイズを固定
root.geometry(f"{cell_size * grid_size}x{cell_size * grid_size}")
root.resizable(False, False)

# 各セルにウィジェットを配置し、固定サイズに
for row in range(grid_size):
    for col in range(grid_size):
        label = ttk.Label(root, text=f"({row}, {col})", relief="solid")
        label.grid(row=row, column=col, sticky=N+S+E+W)

# 各行・列を等しい割合で拡張（固定サイズ内での中央配置）
for i in range(grid_size):
    root.grid_rowconfigure(i, weight=1, minsize=cell_size)
    root.grid_columnconfigure(i, weight=1, minsize=cell_size)

root.mainloop()
