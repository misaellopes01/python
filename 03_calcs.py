# # Integers
# # x = int(input("What's x? "))
# # y = int(input("What's y? "))
# # print(f"{x} + {y} = {x + y}")

# # Float
# x = float(input("What's x? "))
# y = float(input("What's y? "))
# # round a number
# result = round(x / y, 9)
# print(result) # format to get a better readeable number
def main():
    x = int(input("What's x? "))
    print(x,"squared is", square(x))

def square(number):
    # return number * number
    # return number ** 2
    return pow(number, 2)

main()

