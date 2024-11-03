import flet as ft

def main(page: ft.Page):
    def close_app(e):
        # 終了処理
        print("Exiting application...")  # コンソールに出力される
        page.window.destroy()  # アプリケーションを閉じる（修正）

    close_button = ft.ElevatedButton("Close Application", on_click=close_app)  # ElevatedButtonを使用
    page.add(close_button)

ft.app(target=main)
