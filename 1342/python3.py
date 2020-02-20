class Solution:
    def numberOfSteps (self, num):
        step=0
        if(num == 0):
            return 0
        while(num!=1):
            if(num%2==0):  # even
                num = num / 2
                step +=1
            else:
                num = num -1
                step +=1
        return (step+1)
