'''
By Tanvir Hasan Anick
Editorial at https://tanvir002700.wordpress.com/2014/11/26/python-sorting-algorithm/
'''
def bubble_sort(Li,start,last):
    for i in range(start,last):   #take ith position from start
        for j in range(i+1,last): #start jth position from i+1th position
            if  Li[i] > Li[j] :   #compare ith position with jth position
                Li[i] , Li[j] = Li[j] , Li[i] #if ith position is greater than jth position then swap Li[i] & L[j]
             
if __name__=="__main__":
    L=[2,3,4,1,4,8,4,2,7]
    bubble_sort(L,0,len(L))
    print(L)