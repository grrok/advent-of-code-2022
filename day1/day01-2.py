"""
The only complication here is:
  instead of just having a single variable, high_cal, to test against, we've got three values.
Luckily, for any given elf, we only need to compare it against the minimum value of the three, not all three.

As a first pass, let's say:
- We'll just have a list of three. It will be sorted.
- We'll store the value of the minimum as MIN
- Whenever a calorie count exceeds MIN, we overwrite it (arr[0] = new), re-sort the list, then set MIN to arr[0]
"""
def main():
    high_list = [-1, -1, -1]
    min_high = -1
    tmp_count = 0
    with open("resources/day01-input.txt") as f:
        for line in f:
            if line.strip():
                tmp_count += int(line.strip())
            else:
                if tmp_count > min_high:
                    high_list[0] = tmp_count
                    high_list.sort()
                    min_high = high_list[0]
                tmp_count = 0
    print("Highest Calories: " + str(high_list))
    print("Sum: " + str(sum(high_list)))

if __name__ == "__main__":
    main()