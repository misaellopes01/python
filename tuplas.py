import sys

def main():
    n = int(sys.stdin.readline())
    count = 0
    for A in range(1, n):
        count += (n-1)//A
    print(count)

main()
