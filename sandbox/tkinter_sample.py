import tkinter as tk

def send_message():
    # テキストボックスから入力された内容を取得
    user_input = text_input.get()
    
    # 入力された内容を表示エリアに追加
    if user_input:  # 空でない場合のみ追加
        text_display.config(state=tk.NORMAL)  # テキストボックスを編集可能に
        text_display.insert(tk.END, f"You: {user_input}\n")  # ユーザーの入力を追加
        text_display.config(state=tk.DISABLED)  # テキストボックスを読み取り専用に
        text_input.delete(0, tk.END)  # テキストボックスをクリア

# Tkinterウィンドウの設定
root = tk.Tk()
root.title("Text Input Example")

# テキスト表示エリア
text_display = tk.Text(root, height=10, width=50, state=tk.DISABLED)  # 読み取り専用
text_display.pack(pady=10)

# テキスト入力エリア
text_input = tk.Entry(root, width=50)
text_input.pack(pady=5)

# 送信ボタン
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# メインループ
root.mainloop()
