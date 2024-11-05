import yaml
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar

# YAMLデータの読み込み（UTF-8を指定）
with open("layout.yaml", "r", encoding="utf-8") as f:
    layout_data = yaml.safe_load(f)

# ウィンドウの作成
window_data = layout_data['window']
root = ttk.Window()
root.title(window_data['title'])
root.geometry(f"{window_data['width']}x{window_data['height']}")

# スタイルの作成
style = ttk.Style()

# 各要素をidで管理する辞書
frames_dict = {}
elements_dict = {}

# sticky用のショートカット関数
def parse_nswe(nswe_str):
    sticky_dict = {'n': N, 's': S, 'w': W, 'e': E}
    return "".join(sticky_dict[char] for char in nswe_str if char in sticky_dict)

# フレームの作成と配置
for frame_data in layout_data['frames']:
    frame = ttk.Frame(root, bootstyle=frame_data.get('bg_color', 'secondary'))
    frame.grid(row=frame_data['row'], column=frame_data['column'],
               rowspan=frame_data.get('rowspan', 1),
               columnspan=frame_data.get('columnspan', 1),
               sticky=parse_nswe(frame_data.get('nswe', 'nsew')),
               padx=5, pady=5)
    frames_dict[frame_data['id']] = frame  # フレームをidで管理

    # フレーム内の要素を作成
    for element in frame_data['elements']:
        nswe = parse_nswe(element.get('nswe', ''))
        bg_color = element.get('bg_color')
        text_color = element.get('text_color', '#000000')
        widget = None
        
        # スタイル名を作成
        style_name = f"{element['id']}.T{element['type'].capitalize()}"

        # ラベルのスタイル設定
        if element['type'] == "label":
            style.configure(style_name, foreground=text_color)
            widget = ttk.Label(frame, text=element['text'], style=style_name, bootstyle=element.get('style', ''))

        # ボタンのスタイル設定
        elif element['type'] == "button":
            style.configure(style_name, foreground=text_color)
            widget = ttk.Button(frame, text=element['text'], command=lambda: print(element.get('command', '')), style=style_name)

        # エントリのスタイル設定
        elif element['type'] == "entry":
            widget = ttk.Entry(frame, bootstyle="secondary")
            widget.insert(0, element.get('placeholder', ''))

        # チェックボックスのスタイル設定
        elif element['type'] == "checkbox":
            var = StringVar()
            style.configure(style_name, foreground=text_color)
            widget = ttk.Checkbutton(frame, text=element['text'], variable=var, style=style_name)

        # グリッドに配置
        if widget:
            widget.grid(sticky=nswe, padx=5, pady=5)
            elements_dict[element['id']] = widget  # 要素をidで管理

root.mainloop()
