from collections import deque

"""
So... I don't feel the need to create a parser for that stack diagram it gives.
I'll just manually create that in the code.
We'll use collections.deque for this (it replicates LIFO queues with append() and pop(), and in O(1) time).
And, because of that, I've created a modified version of the input file to just have the moves (and not the initial cargo state).
"""

cargo = [
    deque(["H", "T", "Z", "D"]),
    deque(["Q", "R", "W", "T", "G", "C", "S"]),
    deque(["P", "B", "F", "Q", "N", "R", "C", "H"]),
    deque(["L", "C", "N", "F", "H", "Z"]),
    deque(["G", "L", "F", "Q", "S"]),
    deque(["V", "P", "W", "Z", "B", "R", "C", "S"]),
    deque(["Z", "F", "J"]),
    deque(["D", "L", "V", "Z", "R", "H", "Q"]),
    deque(["B", "H", "G", "N", "F", "Z", "L", "D"])
]

def main():
    top_crates = ""
    with open("day05-input-modified.txt") as f:
        for line in f:
            instruction = parse_instruction(line.strip())
            move_crate(instruction[0], instruction[1], instruction[2])
    for i in cargo:
        top_crates += i.pop()
    print(top_crates)

# This will return a 3-tuple, with the values being:
# 0 - The number of crates to move
# 1 - The origin stack
# 2 - The destination stack
# And I've subtracted one from the origin and destination stack numbers to correspond to my cargo array indices
def parse_instruction(line):
    split_line = line.split()
    return (int(split_line[1]), int(split_line[3]) - 1, int(split_line[5]) - 1)

# Essentially processes a single instruction line
# Will move `count` number of crates from `origin` to `destination`
def move_crate(count, origin, destination):
    for _ in range(count):
        cargo[destination].append(cargo[origin].pop())

if __name__ == "__main__":
    main()
