# Loops
## 01 - while
i = 0
while i < 2:
    print(f"[{i}]Hi, there!")
    i += 1

## 02 - for
# for i in [0, 1, 2]:
#     print(f"{i} times")
for i in range(2):
    print(f"{i} times")
# If we will not use the i iteration, we can use _:
# for _ in range(5):
#     print(f"{i} times")

## 03 - use multiplication in print function
print("meow\n" * 2, end="") 