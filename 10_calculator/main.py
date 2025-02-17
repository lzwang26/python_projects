import art
print(art.logo)
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

while True:
    restart = False
    first_num = int(input("What's the first number?"))
    while not restart:
        print("+", "-", "*", "/")
        ope = input("What's the operation?")
        next_num = int(input("What's the next number?"))
        if ope == "+":
            first_num = add(first_num, next_num)
        elif ope == "-":
            first_num = sub(first_num, next_num)
        elif ope == "*":
            first_num = mul(first_num, next_num)
        elif ope == "/":
            first_num = div(first_num, next_num)

        if_continue = input(f"Type \'y\' to continue calculating with {first_num}, "
                           f"or type \'n\' to start a new calculation: ")
        if if_continue == 'y':
            restart = False
        elif if_continue == 'n':
            restart = True


