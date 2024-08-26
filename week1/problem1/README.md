# Construct a Trie from a Collection of Patterns

## Problem Description

**Task:** Construct a trie from a collection of patterns.

**Input Format:** An integer 𝑛 and a collection of strings Patterns = {𝑝1, ..., 𝑝𝑛} (each string is given on a separate line).

**Constraints:**
- 1 ≤ 𝑛 ≤ 100
- 1 ≤ |𝑝𝑖| ≤ 100 for all 1 ≤ 𝑖 ≤ 𝑛
- 𝑝𝑖’s contain only symbols A, C, G, T
- No 𝑝𝑖 is a prefix of 𝑝𝑗 for all 1 ≤ 𝑖 ≠ 𝑗 ≤ 𝑛

**Output Format:** The adjacency list corresponding to Trie(Patterns), in the following format:
- If Trie(Patterns) has 𝑛 nodes, first label the root with 0 and then label the remaining nodes with the integers 1 through 𝑛 − 1 in any order you like.
- Each edge of the adjacency list of Trie(Patterns) will be encoded by a triple: the first two members of the triple must be the integers 𝑖, 𝑗 labeling the initial and terminal nodes of the edge, respectively; the third member of the triple must be the symbol 𝑐 labeling the edge.
- Output each such triple in the format `u->v:c` (with no spaces) on a separate line.