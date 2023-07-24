import sys

def main():
    t = int(sys.stdin.readline())
    myStack = []
    readings(t, myStack)
def readings(testCases, myStack):
    while testCases >= 1:
        numbers = sys.stdin.readline().split()
        if numbers[0] == "2" and myStack:
            myStack.pop()
        elif numbers[0] == "3":
            if not myStack:
                sys.stdout.write("Empty!\n")
            else:
                sys.stdout.write(f"{myStack[-1]}\n")
        elif numbers[0] == "1":
            myStack.append(numbers[1])
        testCases -= 1
main()
# =============================================================================================
# import sys
# from io import StringIO

# def main():
#     t = int(input())
#     myStack = []
#     output_buffer = StringIO()

#     for _ in range(t):
#         numbers = input().split()
#         if numbers[0] == "2" and myStack:
#             myStack.pop()
#         elif numbers[0] == "3":
#             output_buffer.write(f"{myStack[-1]}\n" if myStack else "Empty!\n")
#         elif numbers[0] == "1":
#             myStack.append(numbers[1])

#     sys.stdout.write(output_buffer.getvalue())

# main()
# # ===========================================================================================
# import sys
# from collections import deque

# def main():
#     t = sys.stdin.readline()
#     myStack = deque()

#     for _ in range(int(t)):
#         numbers = input().split()
#         if numbers[0] == "2" and myStack:
#             myStack.pop()
#         elif numbers[0] == "3":
#             sys.stdout.write(f"{myStack[-1]}\n" if myStack else "Empty!\n")
#         elif numbers[0] == "1":
#             myStack.append(numbers[1])

# main()
