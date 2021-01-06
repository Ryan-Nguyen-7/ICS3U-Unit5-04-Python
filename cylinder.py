#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on January 2021
# This program uses a function to calculate
#   the volume of a cylinder

import math


def calculate_volume(radius, height):
    # This function calculates volume of a cylinder

    # process
    volume = math.pi * (radius ** 2) * height

    # output
    return volume


def main():
    # input
    radius_as_string = input("Enter radius (cm): ")
    height_as_string = input("Enter height (cm): ")
    print("")

    try:
        radius_as_number = int(radius_as_string)
        height_as_number = int(height_as_string)

        if radius_as_number > 0 and height_as_number > 0:
            # call function
            volume = calculate_volume(radius_as_number, height_as_number)

            # output
            print("Volume:{}cm²".format(volume))
        else:
            print("Integers must be positive")
    except Exception:
        print("Invalid dimension")


if __name__ == "__main__":
    main()
