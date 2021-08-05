# #include<bits/stdc++.h>
# using namespace std;
# int i;double x,a[105][105];
# const int N = 1e9;
# int main(){
#     scanf("%d,%lf",&i,&x);
#     if(i<0||i>99||x<0||x>N){
#         puts("null");
#         return 0;
#     }
#     a[0][0]=x;
#     for(int j=0;j<i;j++){
#         for(int k=0;k<=j;k++)if(a[j][k]>1){
#             double tmp=(a[j][k]-1)/2;
#             a[j+1][k]+=tmp;
#             a[j+1][k+1]+=tmp;
#         }
#     }
#     double mn=N,mx=0;
#     for(int j=0;j<=i;j++){
#         mn=min(mn,a[i][j]);
#         mx=max(mx,a[i][j]);
#     }
#     printf("%.4lf\n",mx-mn);
#     return 0;
# }