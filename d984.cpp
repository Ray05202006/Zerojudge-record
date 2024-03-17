#include <iostream>

using namespace std;

int main(){
	long long a,b,c;

	while(cin >> a >> b >> c){
		//答案是A的情形 
		if((a>b and a>c and a>b+c) or (c>a and a>b and c<a+b) or (b>a and a>c and b<a+c)){
			cout << ""A"" << endl;
		}
		//答案是B的情形 
		else if((b>a and b>c and b>a+c) or (c>b and b>a and c<a+b) or (a>b and b>c and a<b+c)){
			cout << ""B"" << endl;
		}
		//答案是C的情形 
		else if((c>a and c>b and c>a+b) or (a>c and c>b and a<c+b) or (b>c and c>a and b<a+c)){
			cout << ""C"" << endl;
		}
	}
}