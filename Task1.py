def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        return  "Math Error: Division is not allowed by Zero!"
    else:
        return a / b 
    
def modulo(a, b):
    return a % b

print("Select The Operation:")
print("1. Addition +")
print("2. Subtract -")
print("3. Multiply *")
print("4. Divide /")
print("5. Modulo %")


choice = input("Enter choice (1/2/3/4/5): ")

numOne = int(input("Enter first number: "))
numTwo = int(input("Enter second number: "))

if choice == '1':
    print("Result:", add(numOne, numTwo))
elif choice == '2':
    print("Result:", subtract(numOne, numTwo))
elif choice == '3':
    print("Result:", multiply(numOne, numTwo))
elif choice == '4':
    print("Result:", divide(numOne, numTwo))
elif choice == '5':
    print("Result: ", modulo(numOne, numTwo))
else:
    print("Invalid input")
