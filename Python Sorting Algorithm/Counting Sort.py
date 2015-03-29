'''
By Tanvir Hasan Anick
Editorial at https://tanvir002700.wordpress.com/2014/11/26/python-sorting-algorithm/
'''
def Counting_Sort(Li):
    Max=max(Li) #find out maximum value in the list
    Min=min(Li) #find out minimum value in the list
    freq=[0]*(Max+1) #create new list for count frequency of the value
    for x in Li: #iterate the list
        freq[x]+=1 #count frequency
    sorted_list=[] #create new list for sorted value
    for i in range(Min,Max+1): #iterate minimum to maximum value
        while(freq[i]!=0): #this loop iterate until frequency > 0
            sorted_list.append(i) #insert i in the sorted list if its exist
            freq[i]-=1 #after insertion decrement its frequency
    l=len(Li)
    for i in range(0,l): 
        Li[i]=sorted_list[i] #store the sorted value in main list
 
if __name__=="__main__":
    li=[1,2,100,2,3,45,6,7,8,4,5,100,2,3,4,6,3,199]
    Counting_Sort(li)
    print(li)