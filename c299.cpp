#include <bits/stdc++.h>
using namespace std;

int main(){
	int n,num[200],ans=1;
	//輸入 
	cin >> n;
	for(int i=0;i<n;i++){		
		cin >> num[i];
	}
	//<algorithm>功能:排序
	sort(num,num+n);
	
	//確認是否連號 		 
	for(int i=0;i<n-1;i++){		
		if(num[i+1]!=num[i]+1){
			ans=0;
			break;
		}
	}
	//輸出 
	cout << num[0] << "" "" << num[n-1] << "" "";
	if(ans==0){
		cout << ""no"";
	}
	else{
		cout << ""yes"";
	}
}