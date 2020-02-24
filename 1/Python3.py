class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub,a = 0, 0
        fi = []
        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in nums:
                a = nums.index(sub)
                if a!= i:
                    fi.extend([i,a])
                    return fi              
                else:continue                   
            else:
                continue
# 自己感觉的考点：列表
#运行的时间贼长了：792ms……
