options = input("+ = plus , - - minus, / - division , * - multiplicaton , ** - exponentiation, % - the rest from division: ")
a = int(input("enter the first number: "))
b = int(input("enther the second number: "))
if options == '+':
    print(a + b)
elif options == '-':
    print(a - b)
elif options == '*':
    print(a * b)
elif options == '/':
    if b == 0:
        print("You cant division with 0 !")
    else:
        print(a / b)
elif options == '**':
    print(a ** b)
elif options == '%':
    print(a % b)
else:
    print("You didn't make a options ")
