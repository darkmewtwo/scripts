import time
import concurrent.futures


def f():
    print('start')
    time.sleep(5)
    print('finish')
    

with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
    future1 = executor.submit(f)
    future2 = executor.submit(f)
    future3 = executor.submit(f)

    result1 = future1.result()
    result2 = future2.result()
    result3 = future3.result()

# f()