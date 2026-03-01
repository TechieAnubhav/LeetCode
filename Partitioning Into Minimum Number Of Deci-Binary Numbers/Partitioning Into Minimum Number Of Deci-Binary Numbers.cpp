class Solution {
public:
    int minPartitions(const string& n) {
        char m=n[0];
        for (int i=0; i<n.size(); i++){
            if (n[i]>m){
                m=n[i];
            }
        }
        return m-'0';

}
};
