# python3
import sys


def InverseBWT(bwt):
    # write your code here
    n = len(bwt)

    count_array = []
    first_column = sorted(bwt)
    c = {
        "$": 0,
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0,
    }
    first_occurence = {}
    for i in range(n):
        if first_column[i] not in first_occurence:
            first_occurence[first_column[i]] = i

        count_array.append(c[bwt[i]])
        c[bwt[i]] += 1

    pos = 0
    res = [None] * n
    res[-1] = "$"
    for i in range(n - 1):
        curr_char = bwt[pos]
        offset = count_array[pos]

        res[n - 2 - i] = curr_char
        pos = first_occurence[curr_char] + offset

    return "".join(res)


if __name__ == "__main__":
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))

    # $AAAGGG
