import threading
import sys
import time
# lock = threading.Lock()
from concurrent.futures import ThreadPoolExecutor, thread, ProcessPoolExecutor
import multiprocessing

# print(threading.active_count())

def f(data,sl, lock):
    # print(threading.current_thread())
    print('waiting for lock', sl)
    
    with lock:
        print('acquired lock', sl)
        # lock.acquire()
        print(sl)
        # print('acquired lock')
        # time.sleep(10)
        time.sleep(sl)
        # time.sleep(5)
        print('sleeping......', sl)
        # with lock:
        with open('test.txt', 'w') as f:
            f.write(data)
        # lock.release()
        # print('released lock')
        # print(threading.active_count())
        
        print('done', sl)



if __name__ == "__main__":
    # data = sys.argv[1]
    # t = threading.Thread(target=f, args=(data, ))
    # lock = threading.Lock()
    # locdata = threading.local()
    man = multiprocessing.Manager()
    lock = man.Lock()
    with ProcessPoolExecutor() as executor:
        
        
        data = ['catcatcat', 'dogdogdgodgodgo', 'lionlionlionlion']
        sl = [10, 7, 2]
        results = [executor.submit(f, data[i], sl[i], lock) for i in range(3)]
    # print(dir(t))
    # t.start()
    # t.join()