"""
先打印222，再打印111
你就可以理解成主线程和t1线程分开执行，但
其实是用到了CPU时间片轮转调度，先执行t1，当t1遇到IO操作时，
释放CPU给主线程，当IO完成时，再占用CPU
"""

import threading
import time


# def test():
#     time.sleep(2)
#     print(111)


# if __name__ == "__main__":
#     t1 = threading.Thread(target=test)
#     t1.start()
#     print(222)


class Mythread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        time.sleep(3)
        print(111)


if __name__ == "__main__":
    t1 = Mythread()
    t1.start()
    print(222)
