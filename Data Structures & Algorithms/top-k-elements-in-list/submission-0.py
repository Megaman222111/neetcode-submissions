class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            try: dic[num] += 1
            except: dic[num] = 0
        
        dic = dict(sorted(dic.items(), key = lambda i: i[1], reverse=True))

        print(dic)

        return list(dic.keys())[0:k]