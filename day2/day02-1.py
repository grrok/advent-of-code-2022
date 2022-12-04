"""
Being lazy about it.
There's only nine possible outcomes, so just made a dictionary with them and their corresponding scores.
"""
def main():
    score_dict = {
        "A X": 1 + 3, #(R, R) DRAW
        "A Y": 2 + 6, #(R, P) WIN
        "A Z": 3 + 0, #(R, S) LOSS
        "B X": 1 + 0, #(P, R) LOSS
        "B Y": 2 + 3, #(P, P) DRAW
        "B Z": 3 + 6, #(P, S) WIN
        "C X": 1 + 6, #(S, R) WIN
        "C Y": 2 + 0, #(S, P) LOSS
        "C Z": 3 + 3  #(S, S) DRAW
    }
    score = 0
    with open("day02-input.txt") as f:
        for line in f:
            if line.strip():
                score += score_dict[line.strip()]
    print("Final Score: " + str(score))

if __name__ == "__main__":
    main()