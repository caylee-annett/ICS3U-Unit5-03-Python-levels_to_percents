#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program converts grade levels to percentages


def percentage_calculation(level):
    # This function converts the level to a percentage

    if level == "4+":
        percentage = 97
    elif level == "4":
        percentage = 90
    elif level == "4-":
        percentage = 83
    elif level == "3+":
        percentage = 78
    elif level == "3":
        percentage = 75
    elif level == "3-":
        percentage = 71
    elif level == "2+":
        percentage = 68
    elif level == "2":
        percentage = 65
    elif level == "2-":
        percentage = 61
    elif level == "1+":
        percentage = 58
    elif level == "1":
        percentage = 55
    elif level == "1-":
        percentage = 51
    elif level == "R":
        percentage = 0
    else:
        percentage = -1

    return percentage


def main():
    # This function gets the grade level

    # Input
    print("This program converts grade levels to percentages.")
    print("")
    level_input_string = input("Enter a grade level: ")

    # Call functions
    calculated_percentage = percentage_calculation(level_input_string)

    # Output
    if calculated_percentage == -1:
        print("")
        print("-1")
        print("\nDone.")
    else:
        print("")
        print("Level {0} is {1}%.".format(level_input_string,
                                          calculated_percentage))
        print("\nDone.")


if __name__ == "__main__":
    main()
