# LC - https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # O(n^2)
        # output = [0]*len(temperatures)
        # i=0
        # j=1
        # count = 1
        # while i<len(temperatures):
        #     if j==len(temperatures):
        #         count=0
        #         output[i] = count
        #         i+=1
        #         j = i
        #     elif temperatures[j]>temperatures[i]:
        #         output[i] = count
        #         i+=1
        #         count=0
        #         j = i
        #     count+=1
        #     j+=1
        # return output
        # O(n) time and space
        temp_stack = []
        output = [0]*len(temperatures)
        for pos, val in enumerate(temperatures):
            while temp_stack and temp_stack[-1][1]<val:
                i,v = temp_stack.pop()
                output[i] = pos-i
            temp_stack.append((pos,val))
        return output
            