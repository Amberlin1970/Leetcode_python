class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Product = 1
        Sum = 0
        while (n>=10):
            Product *= n%10
            Sum +=n%10
            n = n//10
        Product *= n
        Sum +=n
        return Product-Sum
