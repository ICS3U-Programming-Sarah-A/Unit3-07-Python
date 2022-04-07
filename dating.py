#!/usr/bin/env python3

# Created by: Sarah
# Created on: Apr, 6th, 2022
# This program uses compound boolean expressions
# to determine if the grandparents will
# allow the user to date their grandchild.


def main():
    # get age from user
    user_age_as_string = input("Enter your age: ")
    print("")

    try:
        # Changing string into integer
        user_age_as_int = int(user_age_as_string)
        # check to see if user_age is in the range of 25 AND 40.
        if user_age_as_int <= 40 and user_age_as_int >= 25:
            print("You can date our grandchild.")
        elif user_age_as_int > 0 and user_age_as_int < 25:
            print("You are too young to date our grandchild.")
        elif user_age_as_int > 40:
            print("You are too old to date our grandchild.")
        else:
            print("Please enter a valid age.")
        # handles errors whenever user enters something that's not an integer.
    except Exception:
        print("{} is not a number.".
              format(user_age_as_string))


if __name__ == "__main__":
    main()
