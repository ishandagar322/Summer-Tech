for i in range(5):
    for x in range(4 - i): 
        print(" ", end ="")
    for y in range(2 * i + 1):
        print("*", end ="")
    print()
for t in range(5):
    for n in range(t):
        print(" ", end ="")
    for s in range(9 - t *2):
        print("*", end ="")
    print()