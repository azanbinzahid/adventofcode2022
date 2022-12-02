# A X Rock 1
# B Y Paper 2
# C Z Sccisors 3

# win 6
# darw 3
# lose 1

move_map = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

move_compare_map = {
    "A": {
        "X": 3 + 0,
        "Y": 1 + 3,
        "Z": 2 + 6
    },
    "B": {
        "X": 1 + 0,
        "Y": 2 + 3,
        "Z": 3 + 6
    },
    "C": {
        "X": 2 + 0,
        "Y": 3 + 3,
        "Z": 1 + 6
    },
}

score = 0
with open('in.txt', 'r') as f:
    for line in f.readlines():
        p1, p2 = line.strip().split(" ")
        score += move_compare_map[p1][p2]

print(score)
