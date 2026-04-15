import argparse

if __name__ == "__main__":
    parse = argparse.ArgumentParser()

    parse.add_argument("--number1", help="First Number")
    parse.add_argument("--number2", help="Second Number")
    parse.add_argument("--operation", help="Operation", choices= ['+','-','*','/'])

    arg = parse.parse_args()

print(arg.number1)
print(arg.number2)
print(arg.operation)

n1 = int(arg.number1)
n2 = int(arg.number2)
result = 0

if arg.operation == '+':
    result = n1 + n2
elif arg.operation == '-':git 
    result = n1 - n2
elif arg.operation == '*':
    result = n1 * n2
elif arg.operation == '/':
    result = n1 / n2
    
print(result)