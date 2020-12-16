import threading
from time import sleep, ctime

class ThreadsRun:

    def loop0(self):
        print("loop0 is start run " + ctime())
        sleep(4)
        print("loop0 is end " + ctime())

    def loop1(self):
        print("loop1 is start run " + ctime())
        sleep(2)
        print("loop1 is end " + ctime())


    def main(self):
        print("main thread is start " + ctime())
        t0 = threading.Thread(target=self.loop0)
        t1 = threading.Thread(target=self.loop1)
        t0.start()
        t1.start()
        t0.join()
        t1.join()
        print("main thtread is end " + ctime())


if __name__ == "__main__":
    run = ThreadsRun()
    run.main()
    print ('this is second push')



