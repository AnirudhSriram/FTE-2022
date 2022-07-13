class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(nlogn) time and O(n) space
        # num = []
        # for i,v in enumerate(nums):
        #     num.append((v,i))
        # num.sort()
        # i = 0
        # j = len(num)-1
        # while i<j:
        #     if num[i][0]+num[j][0] <target:
        #         i+=1
        #     elif num[i][0]+num[j][0]> target:
        #         j-=1
        #     else:
        #         return num[i][1],num[j][1]
        # O(n) time and space
        dictnums = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dictnums:
                return dictnums[complement],i
            dictnums[nums[i]] = i
        