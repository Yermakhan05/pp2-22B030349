def solve(heads, legs):
    if heads >= legs/2:
        return "Wrong!"
    elif legs % 2 != 0:
        return "Wrong!"
    else:
        rabbit = legs/2 - heads
        chicken = heads - rabbit
        return chicken, rabbit


heads = int(input("heads: "))
legs = int(input("legs: "))
print(solve(heads, legs))