"""
We're looking for lines where one range is contained by the other.
In practice, given the format:
  a-b,c-d
This means we're looking for lines where either:
  c >= a && d <= b
  a >=c && b <= d

Also, I'm cutting out the line.strip() check for empty lines, seems unnecessary.

Lots of 0's, 1's, and 2's being thrown around here. Easy to get confused.
"""
def main():
    contain_count = 0
    with open("day04-input.txt") as f:
        for line in f:
            ranges = parse_line(line.strip())
            if range_contain(ranges[0], ranges[1]):
                contain_count += 1
    print("Contained Ranges: " + str(contain_count))

# Will parse line, and return it in the format of a list containing two tuples:
# [(start, end), (start, end)]
def parse_line(line):
    ranges = []
    for i in line.split(","):
        range_ends = i.split("-")
        ranges.append((int(range_ends[0]), int(range_ends[1])))
    return ranges

# Checks to see if one of the ranges is fully contained within the other
def range_contain(range1, range2):
    one_in_two = range1[0] >= range2[0] and range1[1] <= range2[1]
    two_in_one = range2[0] >= range1[0] and range2[1] <= range1[1]
    return one_in_two or two_in_one

if __name__ == "__main__":
    main()