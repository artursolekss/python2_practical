import multiprocessing

def square(number):
    return number * number


def distributed_square(numbers):
    core_no = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=core_no)
    chunk_size = len(numbers) // core_no
    # chunks = [numbers[i:i + chunk_size] for i in range(0,len(numbers),chunk_size)]
    results = pool.map(square,numbers,chunksize=chunk_size)

    pool.close()
    pool.join()
    return results

if __name__ == "__main__":
    numbers = list(range(1,99999999))
    squared_numbers = distributed_square(numbers)
    print(squared_numbers)
