class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if flowerbed==[0] and n<=1:
            return True
        c=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0 and i!=0 and i!=len(flowerbed)-1 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                c+=1
            elif i==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                c+=1
            elif i==len(flowerbed)-1 and flowerbed[i]==0 and flowerbed[i-1]==0:
                flowerbed[i]=1
                c+=1
        return c==n or c>n
