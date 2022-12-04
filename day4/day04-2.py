"""
Just replaced range_contain with range_overlap.
range_overlap works, but, on further reflection, it's too late for me to fully grok it.
Look over it again tomorrow.
"""
def main():
    overlap_count = 0
    with open("day04-input.txt") as f:
        for line in f:
            ranges = parse_line(line.strip())
            if range_overlap(ranges[0], ranges[1]):
                overlap_count += 1
    print("Overlapping Ranges: " + str(overlap_count))

# Will parse line, and return it in the format of a list containing two tuples:
# [(start, end), (start, end)]
def parse_line(line):
    ranges = []
    for i in line.split(","):
        range_ends = i.split("-")
        ranges.append((int(range_ends[0]), int(range_ends[1])))
    return ranges

# Checks to see if the two ranges overlap at all
def range_overlap(range1, range2):
    return range1[0] <= range2[1] and range2[0] <= range1[1]

if __name__ == "__main__":
    main()