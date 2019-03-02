e = 2.7182818284590452353602875

with open("INPUT.TXT") as f:
    for line in f:
        n = int(line)
        print(round(e, n))

