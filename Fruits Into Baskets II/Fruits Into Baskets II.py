class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n=0
        for i in fruits:
            for j in baskets:
                if i<=j:
                    baskets.remove(j)
                    break
            else:
                n+=1
        return n
        
