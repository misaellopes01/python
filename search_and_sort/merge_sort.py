import sys

def main(): 
  randomlyArray = sys.stdin.readline().split(' ')
  randomlyArray = [int(x) for x in randomlyArray]
  sorted_arr = merge_sort(randomlyArray)
  print(sorted_arr)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Conquer (recursively sort subarrays)
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Combine (merge sorted subarrays)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

main()