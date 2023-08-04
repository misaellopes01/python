import sys

def main():
    n = int(sys.stdin.readline())
    number = sys.stdin.readline().split(' ')
    result = 0
    count = 1
    for i in range(1, n):
        if int(number[i]) >= int(number[i - 1]):
            count += 1
        else:
            result = max(result, count)
            count = 1

    result = max(result, count)
    print(result)
       
main()


# import sys

# def main():
#     n = int(sys.stdin.readline())
#     number = sys.stdin.readline().split(' ')
#     result = []
#     count = 1
#     for i in range(n):
#         position = i
#         while position < len(number) - 1:
#           if int(number[position]) <= int(number[position + 1]):
#             count += 1
#             position += 1
#           else:
#               break
#         if count > 0: result.append(count)
#         count = 1
#     sorted_result = sorted(result)
#     print(sorted_result[len(result) - 1])
       
# main()