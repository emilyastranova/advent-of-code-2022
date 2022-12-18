#!/usr/bin/env python3
""" Advent of Code 2022 - Day 17, Problem 1

"""
from rock import Rock
from chamber import Chamber

def main():
    """ Main program """
    # Create a chamber
    chamber = Chamber()
    # Rocks fall in the following order:
    # 1. Horizontal
    # 2. Plus
    # 3. Right angle
    # 4. Vertical
    # 5. Square
    rock_order = ["horizontal", "plus", "right_angle", "vertical", "square"]
    # Begin the simulation
    num_desired_rocks = 10
    current_rock = 0
    while len(chamber) < num_desired_rocks:
        # Get the next rock
        rock_type = rock_order[current_rock]
        rock = Rock(rock_type)
        # Add the rock to the chamber
        chamber.append(rock)
        # Increment the rock counter
        current_rock += 1
        if current_rock == len(rock_order):
            current_rock = 0
        # Get the coordinates of the rock
        rock_coordinates = rock.get_coordinates()
        # Check if the rock is falling

    # Display the chamber
    chamber.display_chamber()

if __name__ == "__main__":
    main()