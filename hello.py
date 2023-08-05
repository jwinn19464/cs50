# name = input("What's your name? ").strip().title()

# print(f"hello, {name}")
def main():
    name = input("What's your name? ")
    hello(name)


def hello(name="world"):
    print("Hello", name)

main()