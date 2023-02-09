def histogram(h):
    for i in range(0, len(h), 1):
        for j in range(1, int(h[i]) + 1, 1):
            print("*", end="")
        print(end="\n")

height = input().split()
histogram(height)