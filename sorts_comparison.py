import random
import timeit
import matplotlib.pyplot as plt

from sorts.insertion_sort import insertion_sort
from sorts.merge_sort import merge_sort
from sorts.tim_sort import timsort


def main():
    random.seed(33)

    arr_sizes = [5, 10, 50, 100, 1000]

    insertion_times = []
    merge_times = []
    timsort_times = []

    for size in arr_sizes:
        print("\nmeasurements for array size (x1000 times):", size)
        arr = random.sample(range(0, 1001), size)

        insertion_time = timeit.timeit(
            lambda: insertion_sort(arr),
            number=1000
        )
        merge_time = timeit.timeit(
            lambda: merge_sort(arr),
            number=1000
        )
        timsort_time = timeit.timeit(
            lambda: timsort(arr),
            number=1000
        )

        insertion_times.append(insertion_time)
        merge_times.append(merge_time)
        timsort_times.append(timsort_time)

        print("insertion_sort:", insertion_time)
        print("merge_sort:", merge_time)
        print("timsort:", timsort_time)

    arr_sizes = list(map(lambda a: str(a), arr_sizes))

    plt.figure(figsize=(10, 6))
    plt.bar(arr_sizes, merge_times, color='green', label='Merge Sort')
    plt.bar(arr_sizes, insertion_times, color='blue', label='Insertion Sort')
    plt.bar(arr_sizes, timsort_times, color='red', label='Timsort')

    plt.xlabel('array size')
    plt.ylabel('time (seconds)')
    plt.title('Sorting Algorithm Comparison (x1000 times)')
    plt.legend()
    plt.show()


main()
