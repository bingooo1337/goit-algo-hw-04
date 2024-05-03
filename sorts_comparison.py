import random
import timeit

from sorts.insertion_sort import insertion_sort
from sorts.merge_sort import merge_sort
from sorts.tim_sort import timsort


def main():
    random.seed(33)

    arr_sizes = [10, 50, 100, 500, 1000]

    for size in arr_sizes:
        print("\nmeasurements for array size (x1000 times):", size)
        arr = random.sample(range(0, 1001), size)

        print(
            "insertion_sort:",
            timeit.timeit(lambda: insertion_sort(arr), number=1000)
        )
        print(
            "merge_sort:",
            timeit.timeit(lambda: merge_sort(arr), number=1000)
        )
        print(
            "timsort:",
            timeit.timeit(lambda: timsort(arr), number=1000)
        )


main()
