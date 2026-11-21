
class Solution:
    def productExceptSelf(self, nums):

        n = len(nums)
        answer = [1] * n

        # Prefix product
        prefix = 1

        for i in range(n):
            answer[i] = prefix
            prefix = prefix * nums[i]

        # Suffix product
        suffix = 1

        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * suffix
            suffix = suffix * nums[i]

        return answer
