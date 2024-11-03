import flet as ft
from multiprocessing import Queue
import threading
import time

def launch_gui(main_to_system_queue, system_to_main_queue):
    def send_data_to_system(data_table):
        """Systemプロセスにdata_tableを送信する共通関数"""
        main_to_system_queue.put(data_table)

    def on_confirm_close(page: ft.Page):
        """ウィンドウが閉じられるときに確認ダイアログを表示"""
        # ダイアログを設定
        def close_app(e):
            print("Window is closing...")
            close_message = {
                "type": "request",
                "command": "close",
                "status": "final",
                "data": {},
                "details": "Closing application"
            }
            send_data_to_system(close_message)
            page.window_destroy()  # ウィンドウを閉じる

        # 閉じる確認ダイアログの表示
        dialog = ft.AlertDialog(
            title=ft.Text("Confirm Exit"),
            content=ft.Text("Are you sure you want to close the application?"),
            actions=[
                ft.TextButton("Cancel", on_click=lambda e: dialog.close()),
                ft.TextButton("OK", on_click=close_app),
            ]
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    def main(page: ft.Page):
        # ウィンドウの閉じる処理を防止し、カスタムの終了処理を設定
        page.window_prevent_close = True
        page.on_disconnect = lambda _: on_confirm_close(page)

        # 入力フィールドとボタンの設定
        input_box = ft.TextField(label="Precision", width=300)
        result_box = ft.Text(value="", width=300)
        
        def on_send_click(e):
            # ユーザーの入力値を取得し、intに変換
            try:
                precision = int(input_box.value)
            except ValueError:
                result_box.value = "Please enter a valid integer for precision."
                page.update()
                return

            # Systemプロセスに送るメッセージを構築
            data_table = {
                "type": "request",
                "command": "calculate",
                "status": "initial",
                "data": {"precision": precision},
                "details": "Starting π calculation"
            }
            send_data_to_system(data_table)  # 共通関数を利用して送信
            input_box.value = ""
            page.update()
        
        # リアルタイムでシステムからの応答を確認するスレッドを作成
        def check_response():
            while True:
                if not system_to_main_queue.empty():
                    response = system_to_main_queue.get()
                    if response["status"] == "completed":
                        result = response["data"]["result"]
                        result_box.value = f"π calculated to specified precision: {result}"
                    page.update()
                time.sleep(1)
        
        threading.Thread(target=check_response, daemon=True).start()

        # ページにUIを追加
        page.add(input_box, ft.ElevatedButton(text="Send", on_click=on_send_click), result_box)

    # Fletアプリケーションの開始
    ft.app(target=main)
