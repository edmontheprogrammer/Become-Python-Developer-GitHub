from multiprocessing import Process
import time


# Processes
def longSquare(num, results):
    time.sleep(1)
    print(num**2)
    print('Finished computing!')


results = {}

p1 = Process(target=longSquare, args=(1, results))
p2 = Process(target=longSquare, args=(2, results))

p1.start()
p2.start()

p1.join()
p2.join()

print(results)  # Outputs empty dictioanry --> {}

Outpust = """        The "freeze_support()" line can be omitted if the program
        is not going to be frozen to produce an executable.
RuntimeError: 
        An attempt has been made to start a new process before the
        current process has finished its bootstrapping phase.

        This probably means that you are not using fork to start your
        child processes and you have forgotten to use the proper idiom
        in the main module:

            if __name__ == '__main__':
                freeze_support()
                ...

        The "freeze_support()" line can be omitted if the program
        is not going to be frozen to produce an executable. """
