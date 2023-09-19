import sys

def main():
  # arr = [38 27 43 3 9 82 10]
  randomlyArray = sys.stdin.readline().split(' ')
  randomlyArray = [int(x) for x in randomlyArray]
  sorted_arr = quick_sort(randomlyArray)
  print(sorted_arr)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

main()