import yaml
import ttkbootstrap as ttk
from tkinter import StringVar

# YAMLデータの読み込み
with open("layout.yaml", "r", encoding="utf-8") as f:
    layout_data = yaml.safe_load(f)

# ウィンドウの作成
window_data = layout_data['window']
root = ttk.Window()
root.title(window_data['title'])
root.geometry(f"{window_data['width']}x{window_data['height']}")
root.resizable(False, False)  # ウィンドウサイズを固定

# スタイルの作成
style = ttk.Style()

# 各要素を配置
for element in layout_data['elements']:
    widget = None
    x = element.get('x', 0)
    y = element.get('y', 0)
    width = element.get('width', None)
    height = element.get('height', None)
    bg_color = element.get('bg_color', None)
    text_color = element.get('text_color', "#000000")
    
    # スタイル名を生成
    style_name = f"{element['id']}.T{element['type'].capitalize()}"

    # 各ウィジェットのタイプに応じて作成
    if element['type'] == "label":
        style.configure(style_name, foreground=text_color, background=bg_color or "white")
        widget = ttk.Label(root, text=element['text'], style=style_name)
        widget.place(x=x, y=y, width=width, height=height)

    elif element['type'] == "button":
        style.configure(style_name, foreground=text_color, background=bg_color or "blue")
        widget = ttk.Button(root, text=element['text'], command=lambda: print(f"{element['id']} clicked"), style=style_name)
        widget.place(x=x, y=y, width=width, height=height)

    elif element['type'] == "entry":
        widget = ttk.Entry(root)
        widget.place(x=x, y=y, width=width, height=height)

    elif element['type'] == "text":
        widget = ttk.Text(root, wrap="word")
        widget.place(x=x, y=y, width=width, height=height)

root.mainloop()
