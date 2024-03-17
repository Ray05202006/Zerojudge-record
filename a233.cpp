#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	int n;
	cin >> n;
	int a[n];
	for(int i=0;i<n;i++){
		scanf(""%d"",&a[i]);
	}
	sort(a,a+n); //內建排序
	for(int i=0;i<n;i++){
		printf(""%d "",a[i]);
	}
}