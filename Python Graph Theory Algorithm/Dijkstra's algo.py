'''
By Tanvir Hasan Anick
Editorial at https://tanvir002700.wordpress.com/2014/11/26/python-graph-theory-algorithm/
'''
from queue import PriorityQueue
def dijkstra(G,src,des):
    dist=[(268435456)]*len(G) #create dist list & initial with inf value
    Q=PriorityQueue() #create priority queue
    dist[src]=0 #source dist is always zero
    Q.put((0,src)) #push source with zero dist in queue
    while(Q.empty()==False): #iterate until queue is empty
        cost,u=Q.get() #take minimum dist, node & pop up
        if(u==des):return dist[des] #if destination find from Q, then return result
        for v,Cost in G[u]: #take all node which is adjacency with u node
            if(dist[v]>cost+Cost): #if present dist greater than to dist[u]+Cost 
                dist[v]=cost+Cost #if u to v is minimum then update dist[v]
                Q.put((dist[v],v)) #push v into Queue
    return -1 #return -1 when source to destination isn't reachable

if __name__=="__main__":
    Node,Edge=map(int,input().split()) #take input number of Node & Edge
    Graph=[[] for i in range(Node+1)] #create 2D list for graph
    for i in range(0,Edge):
        u,v,w=map(int,input().split()) #take input u v w
        Graph[u].append((v,w)) #make u to v adjacency with w weight
        Graph[v].append((u,w)) #make v to u adjacency with w weight
    source,destination=map(int,input().split()) #take input source and destination
    print(dijkstra(Graph, source, destination)) #print shortest path answer




