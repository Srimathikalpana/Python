import threading
import time
def loop():
    for i in range(1,11):
        time.sleep(2)
        print(i)
threading.Thread(target=loop).start()