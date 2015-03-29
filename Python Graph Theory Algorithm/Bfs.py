'''
By Tanvir Hasan Anick
Editorial at https://tanvir002700.wordpress.com/2014/11/26/python-graph-theory-algorithm/
'''
from queue import Queue
def Bfs(G,src,des):
    dist=[-1]*(len(G)+1) #create distance list for save dist
    Q=Queue() #create a queue for maintaining tree level
    dist[src]=0 #source dist set zero
    Q.put(src) #insert source into queue
    while(Q.empty()!=True): #iterate until queue is empty
        u=Q.get() #get front node from queue & pop up
        for v in G[u]: #explore all adjacency node of u
            if(dist[v]==-1): #if v node isn't explore previous then its -1
                Q.put(v) #insert v node in queue
                dist[v]=dist[u]+1 #set dist of v
            if(v==des):return dist[v] # check if destination reach & return dist[v]
    return -1 # return -1 if source to destination isn't reachable

if __name__=="__main__":
    Node,Edge=map(int,input().split()) #take input as Number of node & edge
    Graph=[[] for i in range(Node+1)] #create 2D list for storing Graph
    for i in range(0,Edge):
        u,v=map(int,input().split()) #take u & v node input
        Graph[u].append(v) # make u to v adjacency
        Graph[v].append(u) #make v to u adjacency
    source,destination=map(int,input().split()) #take source and destination
    print(Bfs(Graph, source, destination)) #print shortest path result
    
    
    
