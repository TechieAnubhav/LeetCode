class Solution {
public:
    int smallestRepunitDivByK(int k) {
        if (k%2==0 || k%5==0){
            return -1;
        }
        int rem=0;
        int i=0;
        while (i<=k){
            rem=((rem*10)+1)%k;
            i++;
            if (rem==0){
                return i;
            }
        }
        return -1;
    }
};
