# A X Rock
# B Y Paper
# C Z Sccisors

move_compare_map = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0
    },
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3
    },
}

move_map = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

score = 0
with open('in.txt', 'r') as f:
    for line in f.readlines():
        p1, p2 = line.strip().split(" ")
        score += move_map[p2] + move_compare_map[p1][p2]

print(score)
