#!/usr/bin/env python3

# Created by: Lucas DeBruyn
# Created on: Dec 2022
# This program finds the average of 10 random numbers

import random


def main():
    # This function finds the average of 10 random numbers

    sum_of_numbers = 0
    average = []

    for counter in range(0, 10):
        random_number = random.randint(1, 100)
        average.append(random_number)
        sum_of_numbers = sum_of_numbers + random_number
        print("The random number is {0}:".format(random_number))

    answer = sum_of_numbers / len(average)

    print("\nThe average is {0}".format(answer))
    print("\nDone.")


if __name__ == "__main__":
    main()
