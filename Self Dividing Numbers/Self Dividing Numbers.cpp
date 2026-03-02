class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        int c=0,flag=0;
        vector<int> arr;
        for (int i=left; i<=right; i++){
            int t=i;
            while (t>0){
                int r=t%10;
                if (r==0){
                    flag=1;
                    break;
                }
                if (i%r!=0){
                    flag=1;
                    break;
                }
                t=t/10;
            }
            if (flag==1){
                flag=0;
                continue;
            }
            arr.push_back(i);
        }
        return arr;
    }
};
