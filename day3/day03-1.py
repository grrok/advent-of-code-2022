"""
First thought: manually build a dict or list? Sounds annoying.

string.ascii_letters affords us an easy way to find the priority for a given item type.

The easiest method might be simply: string.ascii_letters.index(x) + 1.
Looks like constructing a dict might be better? O(n) vs O(1)?
    char_dict = {}
    for i in range(len(string.ascii_letters)):
        char_dict[string.ascii_letters[i]] = i + 1
- https://wiki.python.org/moin/TimeComplexity
- https://stackoverflow.com/questions/36868479/python-str-index-time-complexity

Could also potentially use ord()?
    if x.isupper():
        ord(x) - 38
    else:
        ord(x) - 96

Well... the ord() solution seems simpler.
"""

def main():
    total_priority = 0
    with open("day03-input.txt") as f:
        for line in f:
            if line.strip():
                total_priority += get_priority(find_common_type(line.strip()))
    print("Total Priority: " + str(total_priority))

# Gets item type that is in both rucksack compartments
# Is there a better way to do this?
def find_common_type(contents):
    length = int(len(contents) / 2)
    comp_1 = contents[:length]
    comp_2 = contents[length:]
    return set(comp_1).intersection(comp_2).pop()

# Return the priority value of the given item type
def get_priority(item):
    return ord(item) - 38 if item.isupper() else ord(item) - 96

if __name__ == "__main__":
    main()