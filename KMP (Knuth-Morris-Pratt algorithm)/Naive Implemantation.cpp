#include<bits/stdc++.h>
char T[10000];
char P[10000];
int main()
{
    scanf("%s %s",T,P);
    for(int i=0;T[i];i++)
    {
        bool flag=true;
        for(int j=0;P[j];j++)
        {
            if(P[j]!=T[i+j])
            {
                flag=false;
                break;
            }
        }
        if(flag)std::cout<<"match at position "<<i<<std::endl;
    }
    return 0;
}
