'''
By Tanvir Hasan Anick
Editorial at https://tanvir002700.wordpress.com/2014/11/26/python-sorting-algorithm/
'''
def Merge(Li, left, mid, right): 
    left_Li =(Li[left : mid+1]) #divide left side in left_Li list
    right_Li =(Li[mid+1: right+1]) #divide right side in right_Li list
    left_Li.append(2147483647)
    right_Li.append(2147483647)
    i,j = 0,0
    for k in range(left, right+1): #k loop iterate left to right
        if left_Li[i] <= right_Li[j]: #merge condition
            Li[k] = left_Li[i]
            i += 1
        else:
            Li[k] = right_Li[j]
            j += 1
 
def Merge_Sort(Li, left, right): 
    if left < right:
        mid = int((left + right) / 2) 
        Merge_Sort(Li, left, mid) #List divide in left sub problem
        Merge_Sort(Li, mid+1, right) #List divide in right sub problem
        Merge(Li, int(left), int(mid), int(right)) #solve the sub problem
 
if __name__=="__main__":
    Li=[1,2,3,4,5,67,8,-1,2,99,92,-1000,192,-178]
    Merge_Sort(Li, 0, len(Li)-1)
    print(Li)