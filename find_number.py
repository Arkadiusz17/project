find_numer = 40
guessed_number = 0

while find_numer != guessed_number:
    guessed_number = int(input("Give me a number: "))
    if guessed_number < find_numer:
        print("To small a number")
    elif guessed_number > find_numer:
        print("Too many a number")
    else:
        print("Congratulations, you won ! ")

