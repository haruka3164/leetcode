class Solution {
private:
    int n;
    int father[210];
    void init(){
        for(int i=0;i<n;i++){
            father[i]=i;
        }
    }
   int find(int u){
    return u==father[u] ? u : find(father[u]);
   }
   void join(int u,int v){
    u=find(u);
    v=find(v);
    if(u==v) return;
    father[v]=u;
   }
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
      n=isConnected.size();
      init();
      for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(isConnected[i][j]==1) join(i,j);
        }
      }
      unordered_set<int>uset;
      for(int i=0;i<n;i++){
        uset.insert(find(i));
      }
      return uset.size();
    }
};
