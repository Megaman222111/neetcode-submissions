class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            try: dic[num] += 1
            except: dic[num] = 1
        
        print(dic)
        buckets = [[] for _ in range(len(nums)+1)]

        for j,v in dic.items():
            buckets[v].append(j)
        
        ret = []
        for i in range(len(buckets)-1, -1, -1):
            if buckets[i] != 0:
                for n in buckets[i]:
                    ret.append(n)
                    if len(ret) == k:
                        return ret

        return ret