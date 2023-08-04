def main():
    # print_column(3)
    # print_row(4)
    print_pillar(3)

def print_pillar(size):
    for _ in range(size):
        print("[+]" * size)
    # for _ in range(size):
    #   for j in range(size):
    #       print("[+]", end="")
    #   print()


main()