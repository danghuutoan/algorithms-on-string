# python3
import sys

def BWT(text):
    n = len(text)
    arr = []
    for i in range(n):
        arr.append(text[i:]+ text[:i])
    sorted_arr = sorted(arr)
    bwt = ""
    for x in sorted_arr:
        bwt += x[-1]
    return bwt

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))