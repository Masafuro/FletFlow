from multiprocessing import Process, Queue
from interface import launch_gui
from system import system_process

def main():
    # Queueの初期化
    main_to_system_queue = Queue()
    system_to_main_queue = Queue()
    
    # system.pyを起動する
    process = Process(target=system_process, args=(main_to_system_queue, system_to_main_queue))
    process.start()

    # GUIの開始
    launch_gui(main_to_system_queue, system_to_main_queue)

    # プロセスの終了待ち
    process.join()

if __name__ == "__main__":
    main()
