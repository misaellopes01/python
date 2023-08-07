import sys

def main():
    string = sys.stdin.readline()
    left = 0
    right = 0
    for char in string:
        if char == '(':
            left += 1
        elif char == ')': 
            right += 1
        elif left < right:
            right -= 1
        elif left > right:
            left -= 1
            
        
    
    print(left + right)
    
main()
