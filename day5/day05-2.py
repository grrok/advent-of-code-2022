from collections import deque

"""
For this, I just need to update the move_crate method.
I'm still gonna use deques, it'll just be... hackier.
I'll just pop off X number of crates, build a list in reverse, then append them to the destination deque.
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
# Unlike the first challenge, treats `count` crates as a block, doesn't move them individually
#   (well... it does, but from the outside it appears to move them as a block)
def move_crate(count, origin, destination):
    crates = deque()
    for _ in range(count):
        crates.appendleft(cargo[origin].pop())
    for i in crates:
        cargo[destination].append(i)

if __name__ == "__main__":
    main()
