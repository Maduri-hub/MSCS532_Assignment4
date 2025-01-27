def rearrange_heap(arr, size, i):
    largest = i
    left_child = (2 * i) + 1
    right_child = (2 * i) + 2
    if left_child < size and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < size and arr[right_child] > arr[largest]:
        largest = right_child
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        rearrange_heap(arr, size, largest)

def build_max_heap(arr):
    length = len(arr)
    for idx in range((length // 2)- 1, -1, -1):
        rearrange_heap(arr, length, idx)

def heapsort(arr):
    length = len(arr)
    build_max_heap(arr)
    for idx in range(length - 1, 0, -1):
        arr[0], arr[idx] = arr[idx], arr[0]
        rearrange_heap(arr, idx, 0)
    return arr

def display_array(arr, label):
    print(label, arr)

if __name__ == "__main__":
    sample_array = [12, 11, 13, 5, 6, 7]
    display_array(sample_array, "Original Array: ")
    sorted_result = heapsort(sample_array)
    display_array(sorted_result, "Sorted Array: ")
