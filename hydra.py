import threading
def create_thread():
    for x in range(10):
        threading.Thread(target=create_thread).start()
create_thread()