class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int> next;
        stack<int> st;
        vector<int> ans;

        for (int i=nums2.size()-1;i>=0;i--){
            int num=nums2[i];
            while(!st.empty() && st.top()<=num){
                st.pop();

            }
            if ( !st.empty()){
                next[num]=st.top();

            }
            else{
                next[num]=-1;

            }
            st.push(num);

        }
        for(int num : nums1){
            ans.push_back(next[num]);

        }

        return ans;
    }
};