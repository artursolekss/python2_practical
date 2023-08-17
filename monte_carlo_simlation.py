import random
import multiprocessing

def monte_carlo(trials):
    inside_circle = 0
    for _ in range(trials):
        x,y = random.random(), random.random()

        if x**2 + y**2 <=1:
            inside_circle += 1
    return inside_circle

if __name__ == "__main__":
    num_trials = 200000

    trial_per_process = num_trials // multiprocessing.cpu_count()

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(monte_carlo,[trial_per_process] * multiprocessing.cpu_count())


    total_inside_circe = sum(results)
    estimated_pi = 4 * (total_inside_circe/num_trials)
    print("Estimated Pi value",estimated_pi)