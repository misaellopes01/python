import sys

def main():
  orderedList = sys.stdin.readline().split(' ')
  target = int(sys.stdin.readline())

  result = binarySearch(orderedList, target)
  if result != -1:
      print(f'O elemento {target} está na posição {result}.')
  else:
      print(f'O elemento {target} não está na list.')

def binarySearch(list, target):
    start = 0
    end = len(list) - 1

    while start <= end:
        middle = (start + end) // 2

        if int(list[middle]) == target:
            return middle
        elif int(list[middle]) < target:
            start = middle + 1
        else:
            end = middle - 1

    return -1

main()