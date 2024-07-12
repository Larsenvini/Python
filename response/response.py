import validators

def main():
    email = validators.email(input("What's your email address? "))

    if email == True:
        print("Valid")

    else:
        print("Unvalid")

if __name__ == '__main__':
    main()
