from threading import Thread, Lock, Semaphore
from time import sleep

def readString(s):
    l.acquire()
    for i in s:
        print(i)
        sleep(0.5)
    l.release()
        
l=Semaphore(2)      
t1 = Thread(target=readString, args=("python programming language",))
t2 = Thread(target=readString, args=("EASY TO LEARN LANGUAGE",))
t3 = Thread(target=readString, args=("123412345",))


t1.start()
t2.start()
t3.start()
        
        
t1.join()
t2.join()
t3.join()
        



