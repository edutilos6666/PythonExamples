import time
import _thread
from datetime import datetime
import threading
import queue




def example5():
    'priority queue'
    class CustomThread(threading.Thread):
        def __init__(self, thread_id, name, q):
            threading.Thread.__init__(self)
            self.thread_id = thread_id
            self.name = name
            self.q = q


        def run(self):
            print("Starting {0}:{1}".format(self.thread_id , self.name))
            process_data(self.thread_id , self.name, self.q)
            print("Exiting {0}:{1}".format(self.thread_id, self.name))



    exitFlag = 0
    threadLock = threading.Lock()

    def process_data(thread_id , name, q):
        while not exitFlag:
            threadLock.acquire()
            if not q.empty():
                data = q.get()
                threadLock.release()
                print("{0}:{1} processed data {2}".format(thread_id, name, data))
            else:
                threadLock.release()
                time.sleep(1)




    names = ["foo", "bar", "bim", "pako", "edu", "tilos", "leo"]
    q = queue.Queue(10)
    threads = [
        CustomThread(1, "Thread1", q),
        CustomThread(2, "Thread2", q),
        CustomThread(3, "Thread3", q)
    ]

    for th in threads:
        th.start()

    threadLock.acquire()
    for name in names:
        q.put(name)
    threadLock.release()

    while not q.empty():
        pass

    exitFlag = 1
    for th in threads:
        th.join()

    print("Exiting main thread.")
    time.sleep(1)



def example4():
    'uses threading.Thread with threading.Lock()'
    class CustomThread(threading.Thread):
        def __init__(self, thread_id , name, delay = 2, iteration_count = 2):
            threading.Thread.__init__(self)
            self.thread_id = thread_id
            self.name = name
            self.delay = delay
            self.iteration_count = iteration_count

        def run(self):
            print("startinig {0}:{1}".format(self.thread_id , self.name))
            thread_lock.acquire()
            print_time(self.thread_id , self.name, self.delay, self.iteration_count)
            thread_lock.release()


    def print_time(thread_id , name, delay, iteration_count):
        counter = 1
        while counter <= iteration_count:
            time.sleep(delay)
            now = datetime.time(datetime.now())
            print("Time for {0}:{1} = {2} , counter = {3}".format(thread_id , name, now, counter))
            counter += 1

    thread_lock = threading.Lock()

    thread1 = CustomThread(1, "Thread1", 3, 4)
    thread2 = CustomThread(2, "Thread2", 4, 3)
    threads = [thread1, thread2]
    for th in threads:
        th.start()

    for th in threads:
        th.join()

    print("Exiting main thread.")









def example3():
    'uses threading.Thread'
    class CustomThread(threading.Thread):
        def __init__(self, thread_id , name, delay = 2, iteration_count = 3):
            threading.Thread.__init__(self)
            self.thread_id = thread_id
            self.name = name
            self.delay = delay
            self.iteration_count = iteration_count


        def run(self):
            print("Starting {0}:{1}.".format(self.thread_id, self.name))
            print_time(self.thread_id , self.name , self.delay , self.iteration_count)
            print("Exiting {0}:{1}.".format(self.thread_id, self.name))


    def print_time(thread_id , name, delay , iteration_count):
        count = 0
        while count < iteration_count:
            count += 1
            time.sleep(delay)
            now = datetime.time(datetime.now())
            print("time for {0}: {1} = {2} , and count = {3}".format(thread_id, name, now, count))



    thread1 = CustomThread(1, "Thread1", 3, 4)
    thread2 = CustomThread(2, "Thread2", 4, 3)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print("Exiting main thread.")


def example2():
    'uses _thread'
    def print_time(thread_name, delay = 1, iteration_count = 2):
        # iteration_count = 5
        counter = 1
        while counter <= iteration_count:
            time.sleep(delay)
            now = datetime.time(datetime.now())
            print("Time for {0} = {1} , count = {2}".format(thread_name, now, counter))
            counter += 1



    try:
        _thread.start_new_thread(print_time, ("Thread1", 2, 4))
        _thread.start_new_thread(print_time , ("Thread2", 3, 5))
    except:
        print("Cannot start thread.")

    while 1:
        pass




def example1():
    'uses _thread'
    def print_time(thread_name , delay= 1):
        counter = 0
        while counter < 5:
            time.sleep(delay)
            now = datetime.time(datetime.now())
            print("Time for {0} = {1}".format(thread_name, now))
            counter += 1

    try:
        _thread.start_new_thread(print_time, ("Thread1", 2))
        _thread.start_new_thread(print_time, ("Thread2", 3))
    except:
        print("Unable to start thread.")


    while 1:
        pass



