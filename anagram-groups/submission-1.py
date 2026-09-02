class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        used=[]
        for i in range(len(strs)):
            if strs[i] in used:
                continue

            # group = []

            word1 = "".join(sorted(strs[i]))
            group = [strs[i]]
            used.append(strs[i])
            for j in range(i + 1, len(strs)):

                word2 = "".join(sorted(strs[j]))

                if word1 == word2:
                    # group.append(strs[i])
                    group.append(strs[j])
                    used.append(strs[j])

            if group:
                res.append(group)

        return res
        