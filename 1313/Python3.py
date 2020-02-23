class Solution:
    def decompressRLElist(self, nums):
        new_list = []
        length = int(len(nums))
        for i in range(length//2):
            a = nums[2*i]
            b = nums[2*i+1]
            for j in range(a):
                    new_list.append(b)
        return new_list
