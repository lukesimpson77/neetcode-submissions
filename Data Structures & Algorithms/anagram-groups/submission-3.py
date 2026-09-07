class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for x in strs:
            count = [0] * 26
            for c in x:
                count[ord(c) - ord('a')] += 1
            output[tuple(count)].append(x)
        return list(output.values())

            