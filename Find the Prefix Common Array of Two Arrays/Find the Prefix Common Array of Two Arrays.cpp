class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        vector <int> freq(50,0);
        vector <int> ans;
        int c=0;
        for (int i=0; i<A.size(); i++){
            freq[A[i]-1]++;
            freq[B[i]-1]++;
            if (A[i]==B[i]){
                c++;
                ans.push_back(c);
                continue;
            }
            if (freq[A[i]-1]==2){
                c++;
            }
            if (freq[B[i]-1]==2){
                c++;
            }
            ans.push_back(c);
        }
        return ans;
    }
};
