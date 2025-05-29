#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 05, 20, 2025
# This program calculates any user input.


def calculate(symbol, number_1, number_2):
    # Function for calculating where each if is responsible for an operation based upon the symbol entered by the user and then the return of total value called sum
    if symbol == "+":
        sum = number_1 + number_2
        return sum
    if symbol == "-":
        sum = number_1 - number_2
        return sum
    if symbol == "*":
        sum = number_1 * number_2
        return sum
    if symbol == "/":
        sum = number_1 / number_2
        return sum
    if symbol == "%":
        sum = number_1 % number_2
        return sum


def main():
    # In this function, we get input and check it if it is valid
    user_number_1 = input("Enter the first number.")
    # Gets first number
    user_number_2 = input("Enter second number.")
    # Gets second number
    user_symbol = input("Enter math symbol, either +, -, /, *, %")
    # Gets an operation symbol
    try:
        # Checks if the numbers are decimals
        user_number_1 = float(user_number_1)
        user_number_2 = float(user_number_2)
        if (
            user_symbol == "+"
            or user_symbol == "-"
            or user_symbol == "/"
            or user_symbol == "*"
            or user_symbol == "%"
        ):
            # Checks if the symbol entered it right and then continues off the execution
            sum = calculate(user_symbol, user_number_1, user_number_2)
            print(f"The {user_number_1} {user_symbol} {user_number_2} = {sum}")
        elif (
            user_symbol.lower() != "+"
            or user_symbol.lower() != "-"
            or user_symbol.lower() != "/"
            or user_symbol.lower() != "*"
            or user_symbol.lower() != "%"
        ):
            # If the symbol is incorrect, displays the message below
            print("Enter the correct symbol above.")
    except Exception:
        # If the try catch caught an error displays this message.
        print("Should be a decimal number.")


if __name__ == "__main__":
    main()
