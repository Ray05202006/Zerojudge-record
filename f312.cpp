#include <bits/stdc++.h>
using namespace std;

int main(){
	//輸入 
	float a1,b1,c1,a2,b2,c2,n,y1,y2,max=-100000;
	cin >> a1 >> b1 >> c1; 
	cin >> a2 >> b2 >> c2;
	cin >> n;
	//n<=100 故直接爆開  x1=i x2隨之變化 判斷最大值 
	for(int i=0;i<=n;i++){
		y1 = a1*pow(i,2)+b1*i+c1;
		y2 = a2*pow(n-i,2)+b2*(n-i)+c2;
		if(y1+y2>max){
			max = y1+y2;
		}
	}
	//輸出最大值 
	cout << max;
}