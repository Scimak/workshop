import add

def main():
    num1 = input('Enter num1: ')
    num2 = input('Enter num2: ')
    op = input('Enter operation: ')

    print('The answer is:')

    if (op == '+'):
        print(add.add(num1, num2))
    elif (op == '-'):
        print(add.sub(num1, num2))
    elif (op == '/'):
        print(add.mult(num1, num2))
    elif (op == '*'):
        print(add.add(num1, num2))
    else:
        print('invalid operation')