import sys

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
          list = sys.stdin.readline().split(' ')
          list.pop(0)
          for n in range(len(list)):
              list[n] = int(list[n])
          print(f"Case {i+1}: {sum(list)}")

def sum(list):
    if not list:
        return 0
    return list[0] + sum(list[1:])
main()
