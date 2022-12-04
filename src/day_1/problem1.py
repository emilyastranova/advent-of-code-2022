#!/usr/bin/env python3
""" Advent of Code 2022 - Day 1, Problem 1

Load in input.txt and see which Elf is carrying the 
most calories. They are separated by newlines, for example:
Input:  1000
        2000
        3000

        4000
The first elf is carrying 6000 calories and the second elf is
carrying 4000 calories.
"""

def main():
    # Load in input.txt
    raw_input = open("input.txt", "r").read()

    # Split the input by newlines
    input = raw_input.splitlines()

    # Loop through each line and separate the elves by blank lines
    elves = []
    elf = []
    for line in input:
        if line == "":
            elves.append(elf)
            elf = []
        else:
            elf.append(line)

    # Add the last elf
    elves.append(elf)

    # Loop through each elf and calculate their total calories
    for elf in elves:
        total_calories = 0
        for cookie in elf:
            total_calories += int(cookie)

        print("Elf is carrying {} calories".format(total_calories))

    # Find elf with most calories
    max_calories = max(elves, key=lambda x: sum(map(int, x)))
    max_elf = elves.index(max_calories) + 1

    # Print which elf has the most
    print(f"Elf {max_elf} has the most calories with {sum(map(int, max_calories))} calories")

if __name__ == "__main__":
    main()