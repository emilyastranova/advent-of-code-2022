#!/usr/bin/env python3
""" Advent of Code 2022 - Day 1, Problem 1

Load in input.txt and see the top 3 Elves carrying the 
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

    # Find top 3 elves with most calories
    max_calories = sorted(elves, key=lambda x: sum(map(int, x)), reverse=True)[:3]
    max_elves = [elves.index(max_calories[i]) + 1 for i in range(3)]

    # Print which elf has the most
    print(f"Elves {max_elves} have the most calories with {sum(map(int, max_calories[0]))} calories")

    # Print how many calories the top 3 elves have combined
    print(f"Elves {max_elves} have {sum(map(int, max_calories[0])) + sum(map(int, max_calories[1])) + sum(map(int, max_calories[2]))} calories combined")

if __name__ == "__main__":
    main()