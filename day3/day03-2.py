"""
Build a set over every three lines.
Use a counter to verify you're treating every three lines as a single group.
Use the same get_priority func as last time.
I've got an assertion just because... this seems brittle?

For the first ruck in each group, we immediately turn that string into a set.
And we intersect the remaining two strings in the group with that initial set.
According to the instructions, that should always yield only a single common item between all three strings.

The way I'm handling count feels messy, but whatever, it works.
"""

def main():
    total_priority = 0
    count = 0
    ruck_set = set()
    with open("day03-input.txt") as f:
        for line in f:
            count += 1
            if line.strip():
                if not ruck_set:
                    ruck_set = set(line.strip())
                else:
                    ruck_set = ruck_set.intersection(set(line.strip()))
            if count > 2:
                assert len(ruck_set) == 1, "More than one common item type between last three rucks"
                total_priority += get_priority(ruck_set.pop())
                count = 0
    print("Total Priority: " + str(total_priority))

# Return the priority value of the given item type
def get_priority(item):
    return ord(item) - 38 if item.isupper() else ord(item) - 96

if __name__ == "__main__":
    main()