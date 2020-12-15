import threading
from time import sleep,ctime

class NewThreadRun:
    def __init__(self):
        pass

    def loop(self,num,time):
        print("loop" + str(num) + "is start run " + ctime())
        sleep(time)
        print("loop" + str(num) + "is end " + ctime())

    def main(self):
        print("main thread is start run" + ctime())
        loopsList_time = [3,2,1,4]
        threadsList = []
        for i in range(len(loopsList_time)):
 #           func = self.loop(i,loopsList_time[i])
 #           t = threading.Thread(target=func)

            t = threading.Thread(target=self.loop, args=(i,loopsList_time[i]))
            threadsList.append(t)
        for i in range(len(loopsList_time)):
            threadsList[i].start()
        for i in range(len(loopsList_time)):
            threadsList[i].join()
        print ("main thread is end " + ctime())

if __name__ == "__main__":
    runThread = NewThreadRun().main()
