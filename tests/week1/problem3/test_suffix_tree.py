from week1.problem3.suffix_tree import SuffixTree


class TestSuffixTree:
    def test_suffix_tree_construction(self):
        text = "AATCGGGTTCAATCGGGGT"
        tree = SuffixTree(text=text)
        tree.build()
        # for i in range(len(text)):
        #     tree.insert(text, )
        print(tree)
