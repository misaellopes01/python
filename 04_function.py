def main():
    name = input("And what's your name? ")
    hello(name)

def hello(to="World"):
    print("Hello, ", to,"!", sep='')

main()