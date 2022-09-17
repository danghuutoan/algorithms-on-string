from week1.problem2.solution import Trie


class TestSuffixTries:
    def test_suffix_tries(self):
        patterns = ["ATCG", "GGGT"]
        text = "AATCGGGTTCAATCGGGGT"
        trie = Trie()

        for p in patterns:
            trie.insert(p)

        result = trie.match(text=text)
        assert result == [1, 4, 11, 15]
        
