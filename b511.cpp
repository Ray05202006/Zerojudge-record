#include <bits/stdc++.h>
using namespace std;

//從小到大依序找(最左邊最小) 使用遞迴
void s(int coin[],int num[],int c,int n,int c_k){
//coin為硬幣面額的陣列 num為硬幣數量的陣列 c為要換的金額 n為面額種類數量 c_k為當前面額種類 

//	printf(""test:"");
//	for(int i=0;i<n;i++){
//		printf(""%d "",num[i]);
//	}
//	printf(""\n"");
	int sum;
	sum=0;
	//如果第一種硬幣得總和超過金額，便結束遞迴
	if(c<coin[0]*num[0]){	 
		return;
	}
	//算目前總和 
	for(int i=0;i<=c_k;i++){	
			sum += coin[i]*num[i];
	}
//	printf(""test:"");
//	printf(""%d\n"",sum);
	//如果目標金額小於目前總額，當前種類的數量歸零，前一種數量加一 
	if(c<sum){
		num[c_k]=0;
		num[c_k-1]+=1;
		return s(coin,num,c,n,c_k-1);
	}
	/*如果目前是最後一種，判斷剩餘金額是否被最後一種整除  
	  如果可以，紀錄數量並輸出結果 
	*/
	if(c_k+1==n){
		if((c-sum)%coin[c_k]==0){
			num[c_k]=(c-sum)/coin[c_k];
			printf(""("");
			for(int i=0;i<n-1;i++){
				printf(""%d,"",num[i]);
			}
			printf(""%d)"",num[n-1]);
			printf(""\n"");
		}
		//最後一個歸零，前一個加一，return程式 
		num[c_k]=0;
		num[c_k-1]+=1;
//		printf(""%d\n"",num[c_k]);
		return s(coin,num,c,n,c_k-1);
	}
	//因為從小到大，故直接推進到下一個種類 
	return s(coin,num,c,n,c_k+1);
}

int main(){
	//設變數 
	int N,C;
	
	//輸入 
	cin >> N;
//	scanf(""%d %d"",&C,&N);
	int coin[N];
	int num[N]={0};
	for(int i=0;i<N;i++){
		scanf(""%d"",&coin[i]);
	}
	cin >> C;
	s(coin,num,C,N,0);	
} 