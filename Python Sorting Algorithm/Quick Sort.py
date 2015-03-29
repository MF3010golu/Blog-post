'''
By Tanvir Hasan Anick
Editorial at https://tanvir002700.wordpress.com/2014/11/26/python-sorting-algorithm/
'''
def Partition(Li,left,right): #partition for divide the list
    pivot=Li[right] #consider last element as pivot
    i=left-1;
    for j in range(left,right): # loop iteration left to right-1
        if Li[j]<=pivot:
            i=i+1
            Li[i],Li[j]=Li[j],Li[i]
    Li[i+1],Li[right]=Li[right],Li[i+1]
    return i+1
 
def Quick_Sort(Li,left,right):
    if left<right: 
        q=Partition(Li, left, right) #find out the partition point
        Quick_Sort(Li, left, q-1) #solve left sub problem part
        Quick_Sort(Li, q+1, right) #solve right sub problem part
 
if __name__=="__main__":
    Li=[1,2,3,4,5,67,8,-1,2,99,92,-1000,192,-178]
    Quick_Sort(Li, 0, len(Li)-1)
    print(Li)