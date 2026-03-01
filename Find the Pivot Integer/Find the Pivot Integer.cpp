class Solution {
public:
    int pivotInteger(int& n) {
        double a=sqrt((n*(n+1))/2);
        if (a-ceil(a)==0){
            return int(a);
        }
        else{
            return -1;
        }
    }
};
