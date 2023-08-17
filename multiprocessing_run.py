import multiprocessing
import time
import random

def square(number):
    return number * number


def distributed_square(numbers):
    core_no = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=core_no)
    chunk_size = len(numbers) // core_no
    # chunks = [numbers[i:i + chunk_size] for i in range(0,len(numbers),chunk_size)]

    start_time = time.time()
    results = pool.map(square,numbers,chunksize=5000)
    result_time = time.time() - start_time

    pool.close()
    pool.join()
    return result_time

if __name__ == "__main__":
    # numbers = list(range(1,99999999))

    random.seed(10)
    numbers = random.sample(range(1,9999999999),1000000000)
    res_time = distributed_square(numbers)
    print(res_time)
