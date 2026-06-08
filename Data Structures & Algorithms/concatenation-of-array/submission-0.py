class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2*len(nums))

        second_half = len(nums) 

        for i in range(0,len(nums)):
            ans[i] = nums[i]
            ans[second_half] = nums[i]
            second_half +=1
        return ans


            