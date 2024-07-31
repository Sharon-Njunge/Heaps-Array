import heapq
def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    return sorted_arr
    

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]