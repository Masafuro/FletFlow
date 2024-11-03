import time
import math

def calculate_pi(precision):
    """指定された精度でπを計算する関数"""
    return round(math.pi, precision)

def process_request(data_table):
    """受け取ったデータテーブルを処理し、結果のレスポンスを生成する共通関数"""
    command = data_table.get("command")
    if command == "calculate":
        # データの内容に基づきπの計算を行う
        precision = data_table["data"].get("precision", 2)
        pi_result = calculate_pi(precision)

        # 返信メッセージの生成
        response_table = {
            "type": "response",
            "command": "calculate",
            "status": "completed",
            "data": {"result": pi_result},
            "details": f"Calculated π to {precision} decimal places"
        }
        return response_table
    else:
        # 未対応のコマンドへの対応
        return {
            "type": "response",
            "command": command,
            "status": "error",
            "data": {},
            "details": f"Unknown command: {command}"
        }

def system_process(main_to_system_queue, system_to_main_queue):
    while True:
        if not main_to_system_queue.empty():
            # Queueからメッセージを受け取る
            data_table = main_to_system_queue.get()
            print(f"System received: {data_table}")

            # 受け取ったデータを共通関数で処理
            response_table = process_request(data_table)

            # 結果を返信用Queueに送信
            system_to_main_queue.put(response_table)

        time.sleep(1)  # 無限ループを少し緩やかにする
