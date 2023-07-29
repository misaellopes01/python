import sys

def main():
    t = int(sys.stdin.readline())
    numbers = sys.stdin.readline().split(' ')
    for n in range(len(numbers)):
              numbers[n] = int(numbers[n])
    print(pairwise(numbers))
    
def pairwise(ns):
    found = set()
    for number in ns:
        if number in found:
              return "NO"
        found.add(number)
    return "YES"

main()