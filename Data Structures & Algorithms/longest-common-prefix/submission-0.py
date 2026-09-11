class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        while True:
            try:
                pre = ""
                for x in range(len(strs[0])):
                    for y in strs:
                        if strs[0][x] != y[x]:
                            break
                    if strs[0][x] != y[x]:
                            break
                    pre = pre + strs[0][x]
                return pre
            except Exception as e:
                return pre

                 
        