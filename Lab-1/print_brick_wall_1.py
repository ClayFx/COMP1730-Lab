
## procedure to print two overlapping brick rows:
def print_bricks():
    print("--+-----+---")
    print("  |     |")
    print("-----+-----+")
    print("     |     |")


## repeat the two rows three times to make a higher wall:
for i in range(3):
    print_bricks()
