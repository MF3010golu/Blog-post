'''
By Tanvir Hasan Anick
Editorial at https://tanvir002700.wordpress.com/2014/11/26/python-graph-theory-algorithm/
'''
Graph=[] #this list for storing for graph
visit=[] #this list for visit checking
paretn=[] #this list for save parent
def dfs(u): 
    global visit #using global variable
    global parent 
    if(visit[u]):return #if this u node previously visited then return
    visit[u]=True #now u node mark as visited
    for v in Graph[u]: #take all node v which is adjacency with u
        parent[v]=u #take v parent's u
        dfs(v) #call next depth with v
    
def dfs_search(N):
    global parent 
    global visit
    visit=[False]*(N+1) #initial visit list with false
    parent=[-1]*(N+1)#initial parent list with -1
    for u in range(N):
        if(visit[u]==False):dfs(u) #dfs calling
    
if __name__=="__main__":
    Node,Edge=map(int,input().split())
    Graph=[ [] for i in range(Node+1)]
    for i in range(Edge):
        u,v=map(int,input().split())
        Graph[u].append(v)
    dfs_search(Node)
