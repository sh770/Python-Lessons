def print_multiplication_table(n):
    width = len(str(n * n)) + 1
    print(" " * (width - 1), end='')
    for i in range(1, n+1):
        print("{0:>{width}}".format(i, width=width), end='')
    print()
    print(" " * (width - 1) + "|" + "-" * (width * n))
    for i in range(1, n+1):
        print("{0:>{width}}".format(i, width=width), end='')
        for j in range(1, n+1):
            print("{0:>{width}}".format(i*j, width=width), end='')
        print()

print_multiplication_table(10)
