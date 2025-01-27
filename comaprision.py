import time
import random
from heap import heapsort

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left_part = [x for x in arr if x < pivot]
    right_part = [x for x in arr if x > pivot]
    return quicksort(left_part) + [pivot] + quicksort(right_part)

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid_point = len(arr) // 2
    left_half = mergesort(arr[:mid_point])
    right_half = mergesort(arr[mid_point:])
    return merge_lists(left_half, right_half)

def merge_lists(left, right):
    merged = []
    left_idx = right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged

def measure_sort_time(sort_func, data):
    start_time = time.time()
    sort_func(data[:])
    end_time = time.time()
    return end_time - start_time

def average_sort_time(sort_func, data, repetitions=5):
    total_time = 0
    for _ in range(repetitions):
        total_time += measure_sort_time(sort_func, data)
    return total_time / repetitions

test_sizes = [1000, 5000, 10000, 50000]
array_types = ["sorted", "reverse", "random"]

for size in test_sizes:
    for arr_type in array_types:
        if arr_type == "sorted":
            array = list(range(size))
        elif arr_type == "reverse":
            array = list(range(size, 0, -1))
        elif arr_type == "random":
            array = [random.randint(0, size) for _ in range(size)]

        print(f"Array Size: {size}, Array Type: {arr_type}")
        print(f"Heapsort: {average_sort_time(heapsort, array):.8f} seconds")
        print(f"QuickSort: {average_sort_time(quicksort, array):.8f} seconds")
        print(f"MergeSort: {average_sort_time(mergesort, array):.8f} seconds\n")
