class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ones = [1] * numOnes
        zeros = [0] * numZeros
        negs = [-1] * numNegOnes
        res = ones + zeros + negs
        return sum(res[:k])