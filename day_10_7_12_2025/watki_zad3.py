import os
from concurrent.futures import ProcessPoolExecutor


# GIL

def worker(i):
    print(f"Proces: {i} w PID: {os.getpid()}")


def main():
    with ProcessPoolExecutor(max_workers=5) as executor:
        for i in range(20):
            executor.submit(worker, i)


# powinno byc uruchmiane w formule if main
if __name__ == '__main__':
    # with ProcessPoolExecutor(max_workers=5) as executor:
    #     for i in range(20):
    #         executor.submit(worker, i)
    main()
