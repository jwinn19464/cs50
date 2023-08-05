# x = float(input("Give me a number "))
# y = float(input("Give me another number "))

# z = round(x / y, 3)
# # print(f"{z:,}")
# print(z)

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)

main()