import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        output = 0
        number = sys.stdin.readline().strip()
        for char in number:
            n = int(char)
            output += n
        print(output)

main()