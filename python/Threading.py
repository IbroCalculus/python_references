
#CHECK: Python Full Course: 5:40:00

import threading as thd

#============= VIEW ACTIVE THREADS ====================
print(f'NUMBER OF ACTIVE THREADS: {thd.active_count()}')

#============= VIEW LIST OF ACTIVE THREADS ====================
print(f'LIST OF ACTIVE THREADS: {thd.enumerate()}')


#===================== EXAMPLE: RUN 3 TASKS CONCURRENTLY ==============
import  time
def firstTimer():
    for i in range(1,10):
        time.sleep(1)
        print(f'FIRST TIMER: {i}\n')

def secondTimer():
    for i in range(1,10):
        time.sleep(1)
        print(f'SECOND TIMER: {i}\n')

def thirdTimer():
    for i in range(1,10):
        time.sleep(1)
        print(f'THIRD TIMER: {i}\n')

print("Starting Thread")
firstThread = thd.Thread(target=firstTimer, args=())    #arg=() Optional, if function takes in parameter
firstThread.start()

secondThread = thd.Thread(target=secondTimer, args=())
secondThread.start()

thirdThread = thd.Thread(target=thirdTimer, args=())
thirdThread.start()


#============================ CHECK DURATION OF MAIN THREAD ===========================
print(f'Main thread ran for {time.perf_counter()} seconds')


#==================== Thread Synchronization =============================
#This is a concept where one thread waits for another to finish execution before it resumes

firstThread.join()      #Main thread must wait for firstThread to finish executing before it can proceed
print(f'Main thread ran for {time.perf_counter()} seconds')
