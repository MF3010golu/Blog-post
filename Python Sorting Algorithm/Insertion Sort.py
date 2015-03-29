'''
By Tanvir Hasan Anick
Editorial at https://tanvir002700.wordpress.com/2014/11/26/python-sorting-algorithm/
'''
def insertion_sort(Li,start,last):
    for i in range(start+1,last): # ith postion start with start+1
        key=Li[i] #insert Li[i] into the sorted sequence Li[0....... last-1]
        j=i-1
        while j>=start and Li[j]>key:
            Li[j+1]=L[j]
            j-=1
            Li[j+1]=key
 
if __name__=="__main__":
    L=[10,9,8,7,6,5,4,3,2,1]
    insertion_sort(L,0,len(L))
    print(L)