class Solution:
    def hammingWeight(self, n: int) -> int:
        NumberofOnes = 0
        while n>0:
            if n%2 ==1:
                NumberofOnes += 1
            n//=2
        return NumberofOnes
        

        

        