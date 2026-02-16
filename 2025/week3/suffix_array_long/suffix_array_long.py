# python3
import sys

char_set = ['$','A', 'C', 'G', 'T']

def SortCharacters(S):
    count = {}
    for c in char_set:
        count[c] = 0
    order = [None]* len(S)
    for i in range (len(S)):
        if S[i] not in count:
            count[S[i]] = 0

        count[S[i]] = count[S[i]] + 1

    for i, c in enumerate(char_set):
        if i > 0:
            count[c] = count[c] + count[char_set[i-1]]
    

    for i in range(len(S) -1, -1, -1):
        c = S[i]
        count[c] = count[c] - 1
        order[count[c]] = i
 
    
    return order



def ComputeCharClasses(S, order):
    cls = [None] * len(S)
    cls[order[0]] = 0
    for i in range(1, len(S)):
        if S[order[i]] != S[order[i -1]]:
            cls[order[i]] = cls[order[i-1]] +1 
        else:
            cls[order[i]] = cls[order[i-1]]
    return cls

def SortDoubled(S, L, order, cls):
    n = len(S)
    count = [0] * n
    newOrder = [None] * n
    for i in range(n):
        count[cls[i]] = count[cls[i]] + 1

    for j in range(1, n):
        count[j] = count[j] + count[j-1]
    for i in range(n -1, -1, -1):
        start = (order[i] - L  + n) % n
        cl = cls[start]
        count[cl] = count[cl] -1
        newOrder[count[cl]] = start
    return newOrder


def UpdateClasses(newOrder, cls, L):
    n = len(newOrder)
    newClass = [None] * n
    newClass[newOrder[0]] = 0

    for i in range(1, n):
        cur = newOrder[i]
        prev = newOrder[i-1]
        mid = (cur + L) % n
        midPrev= (prev + L) % n
        if cls[cur] != cls[prev] or cls[mid] != cls[midPrev]:
            newClass[cur] = newClass[prev] + 1
        else:
            newClass[cur] = newClass[prev]
        
    return newClass

def BuildSuffixArray(S):
    order = SortCharacters(S)
    cls = ComputeCharClasses(S, order)

    L = 1
    n = len(S)
    while L < 2*n:
        order = SortDoubled(S, L, order, cls)
        cls = UpdateClasses(order, cls, L)
        L = 2*L
    return order

def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  result = BuildSuffixArray(text)
  # Implement this function yourself
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
