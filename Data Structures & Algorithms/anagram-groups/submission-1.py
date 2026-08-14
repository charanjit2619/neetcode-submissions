class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams = {} Instead of defining a dictionary, use defaultdict
        anagrams = defaultdict(list)

        for word in strs:
            anagrams["".join(sorted(word))].append(word)
            #Because of defaultdict, below initialization is not needed
            # else:
            #     anagrams["".join(sorted_word)] = [word]

        return list(anagrams.values())