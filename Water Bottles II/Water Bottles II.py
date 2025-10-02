class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        s=0
        e=0
        while numBottles>0:
            e=e+numBottles
            s=s+numBottles
            numBottles=0
            if e>=numExchange:
                e=e-numExchange
                numExchange+=1
                numBottles+=1
        return s
