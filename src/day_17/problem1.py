#!/usr/bin/env python3
""" Advent of Code 2022 - Day 17, Problem 1

"""
from rock import Rock
from chamber import Chamber

def main():
    """ Main program """
    # Create a chamber
    chamber = Chamber()
    # Add a rock to the chamber
    chamber.append(Rock(0, 0, "vertical"))
    chamber.append(Rock(4, 1, "right_angle"))
    # Display the chamber
    chamber.display_chamber()

if __name__ == "__main__":
    main()