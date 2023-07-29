x = int(input("X value: "))
y = int(input("Y value: "))
# if x < y or x > y:
# if x < y and x > 12:
if x != y:
    print(f"x[{x}] is not equal to y[{y}]")
else:
    print(f"x[{x}] is equal to y[{y}]")

match x:
    case 3:
        print("Odd")
    case _:
        print("Something else")