import sys

def main():
    # strip() to remove the new line char
    numbers = sys.stdin.readline().strip()
    total = 0
    for i in range(1 << (len(numbers) - 1)):
        remainders = ""
        for f in range(len(numbers)):
            remainders += numbers[f]
            if i & (1 << f) and f < len(numbers) - 1:
                remainders += '+'
        total += eval(remainders)   
    print(total)
           
main()