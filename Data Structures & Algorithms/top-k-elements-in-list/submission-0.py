class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first create the hash map for the counts
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        #once thats done create the frequency bucket sort
        #key first then value
        for num, count in counts.items():
            freq[count].append(num)

        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

