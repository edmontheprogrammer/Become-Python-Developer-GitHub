import threading
import time


# Threads
def longSquare(num):
    time.sleep(1)
    return num**2


print([longSquare(n) for n in range(0, 5)])

t1 = threading.Thread(target=longSquare, args=(1, ))
t2 = threading.Thread(target=longSquare, args=(2, ))

t1.start()
t2.start()

t1.join()
t2.join()


def longSquare(num, results):
    time.sleep(1)
    results[num] = num


results = {}

t1 = threading.Thread(target=longSquare, args=(1, results))
t2 = threading.Thread(target=longSquare, args=(2, results))

t1.start()
t2.start()

t1.join()
t2.join()

print(results)
