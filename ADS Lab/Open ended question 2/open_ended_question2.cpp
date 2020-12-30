/* In the given range [L, R], print all numbers having unique digits. e.g. In range 10 to 20 should print all numbers except 11.

Example 1:

Input:
L = 10
R = 20

Output:
10 12 13 14 15 16 17 18 19 20

Explanation:
The number 11 has two 1 therefore
11 is not a unique number.

Example 2:

Input:
L = 1
R = 9

Output:
1 2 3 4 5 6 7 8 9

Explanation:
All the Numbers are unique.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function uniqueNumbers() which takes two integers L and R as an input parameter 
and returns the list/vector of all the unique numbers present between L to R.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= L <= R <= 10^4
*/
#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int main() {
	int t;
//	cin >> t;
//	while(t--)
//	{
	    int m, n;
	    cout<<"L = ";
	    cin >> m ;
	    cout<<"R = ";
		cin >> n;
	    for(int i = m;i<=n;i++)
	    {
	        int temp = i, flag = 0;
	        vector<int>A;
	        while(temp>0)
	        {
	            int mod = temp%10;
	            A.push_back(mod);
	            temp = temp/10;
	        }
	        for(int j=0;j<A.size()-1;j++)
	        {
	            if(A.size()>2)
	            {
					if(A[j] == A[j+1] || A[0] == A[2])
	                {
	                    flag = 1;
	                    break;
	                }
				}
                if(A.size()<=2)
                {
                    if(A[j] == A[j+1])
                    {
	                    flag = 1;
	                    break;
                    }
                }
	        }
	        
	        if(flag==0)
	            cout << i << " ";
	    }
	    cout << endl;
	    
	//}
	return 0;
}
