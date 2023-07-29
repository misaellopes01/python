def main():
    n = int(input("Type a number: "))
    # Ternary operator in python
    print("Even") if is_even(n) else print("Odd")

def is_even(number):
    return number % 2 == 0
    #return True if number % 2 == 0 else False
    
main()