"""
No need to parse the whole file (I mean, in this case it's fine, we know the file's just 2238 lines and 233 total elves, but still...).
So we just parse it line-by-line, using the blank lines as delimiters.
Use tmp_count to store the calorie count for a given elf as we're working through his food items.
Use high_cal to store the highest calorie count we've seen so far.
And just test tmp_count against high_cal whenever we hit the delimiter.
"""
def main():
    tmp_count = 0
    high_cal = -1
    with open("resources/day01-input.txt") as f:
        for line in f:
            if line.strip():
                tmp_count += int(line.strip())
            else:
                high_cal = max(high_cal, tmp_count)
                tmp_count = 0
    print("Highest Calories: " + str(high_cal))

if __name__ == "__main__":
    main()