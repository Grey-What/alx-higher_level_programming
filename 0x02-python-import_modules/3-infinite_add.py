#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    count = len(sys.argv) - 1
    total = 0
    for n in range(count):
        total = total + int((sys.argv[n + 1]))
    print(total)
