import sys

def main():
    t = int(sys.stdin.readline())
    grid = ['' for _ in range(t)]
    for i in range(t):
        grid[i] = sys.stdin.readline()
    
    for row in grid:
        hashtag = 0
        dots = 0
        for i in range(len(row)):
            if row[i] == '#':
                for j in range(i, i + 6):
                    if j >= len(row):
                        break
                    if row[j] == '#':
                        hashtag += 1
                    else:
                        dots += 1
                if hashtag >= 4 and dots >= 2:
                    break
        if hashtag < 4:
            hashtag = 0
            dots = 0
        else:
            break

    result = 'Yes' if hashtag >= 4 and dots <= hashtag else 'No'
    print(result)

if __name__ == "__main__":
    main()
