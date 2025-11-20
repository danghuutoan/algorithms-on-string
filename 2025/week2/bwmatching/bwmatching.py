# python3
import sys

char_list = ['$', "A", "C", "G", "T"]
char_list_idx_mapping = {
  "$": 0,
  "A": 1,
  "C": 2,
  "G": 3,
  "T": 4,
}

def PreprocessBWT(bwt):
  """
  Preprocess the Burrows-Wheeler Transform bwt of some text
  and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position 
        of this character in the sorted array of 
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
  """
  char_count = {
    "$": 0,
    "A": 0,
    "C": 0,
    "G": 0,
    "T": 0,
  }
  starts = [0]* len(char_list)
  occ_counts_before = []
  occ_counts_before.append([0,0,0,0,0])
  
  # Implement this function yourself
  first_column = sorted(bwt)

  for i, c in enumerate(first_column):
    if char_count[c] == 0:
      starts[char_list_idx_mapping[c]] =i
    char_count[c] += 1
  
  for i, c in enumerate(bwt):
    new = occ_counts_before[-1].copy()
    new[char_list_idx_mapping[c]] += 1
    occ_counts_before.append(new)
  return starts, occ_counts_before

def CountOccurrences(pattern, bwt, starts, occ_counts_before):
  """
  Compute the number of occurrences of string pattern in the text
  given only Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - starts and occ_counts_before.
  """
  # Implement this function yourself
  top = 0
  bottom = len(bwt) -1
  while top <= bottom:
    if pattern != '':
      symbol = pattern[-1]
      pattern = pattern[:-1]
      top = starts[char_list_idx_mapping[symbol]] + occ_counts_before[top][char_list_idx_mapping[symbol]]
      bottom = starts[char_list_idx_mapping[symbol]] + occ_counts_before[bottom+1][char_list_idx_mapping[symbol]] -1
    else:
      return bottom - top + 1
  return 0
     


if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  # Preprocess the BWT once to get starts and occ_count_before.
  # For each pattern, we will then use these precomputed values and
  # spend only O(|pattern|) to find all occurrences of the pattern
  # in the text instead of O(|pattern| + |text|).  
  starts, occ_counts_before = PreprocessBWT(bwt)
  occurrence_counts = []
  for pattern in patterns:
    occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
  print(' '.join(map(str, occurrence_counts)))
