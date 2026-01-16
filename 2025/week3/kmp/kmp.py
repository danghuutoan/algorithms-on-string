# python3
import sys


def compute_prefix_function(P):

    border = 0
    n = len(P)
    s = [0] * n
    for i in range(1, n):
        while border > 0 and P[i] != P[border]:
            border = s[border - 1]
        if P[i] == P[border]:
            border = border + 1
        else:
            border = 0
        s[i] = border
    return s


def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    result = []
    if len(pattern) > len(text):
        return []
    
    tmp = pattern + "$" + text

    prefix_funtion = compute_prefix_function(tmp)
    pattern_len = len(pattern)
    for i in range(len(prefix_funtion)):
        if prefix_funtion[i] == pattern_len:
            result.append(i - 2*pattern_len)

    return result


if __name__ == "__main__":
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
