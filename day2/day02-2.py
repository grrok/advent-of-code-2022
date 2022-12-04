"""
Just changed the dictionary around.
Lazy approach still applies.
"""
def main():
    score_dict = {
        "A X": 3 + 0, #(R, S) LOSS
        "A Y": 1 + 3, #(R, R) DRAW
        "A Z": 2 + 6, #(R, P) WIN
        "B X": 1 + 0, #(P, R) LOSS
        "B Y": 2 + 3, #(P, P) DRAW
        "B Z": 3 + 6, #(P, S) WIN
        "C X": 2 + 0, #(S, P) LOSS
        "C Y": 3 + 3, #(S, S) DRAW
        "C Z": 1 + 6  #(S, R) WIN
    }
    score = 0
    with open("day02-input.txt") as f:
        for line in f:
            if line.strip():
                score += score_dict[line.strip()]
    print("Final Score: " + str(score))

if __name__ == "__main__":
    main()