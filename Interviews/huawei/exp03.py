# queue<int>q;
#     q.push(m);vis[m]=1;
#     while(!q.empty()){
#         int u=q.front();q.pop();
#         for(auto v:g[u])if(vis[v]){
#             cout<<-1<<endl;
#             return 0;
#         }else{
#             q.push(v);
#             ans.push_back(v);
#             vis[v]=1;
#         }
#     }