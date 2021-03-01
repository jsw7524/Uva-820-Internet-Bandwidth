class Edge(object):
    def __init__(self,s,e,c):
        self.v1=s
        self.v2=e
        self.capacity=c
        self.currentFlow=0
    def GetAnotherVertex(self, v):
        if v==self.v1:
            return self.v2
        elif v==self.v2:
            return self.v1
        return -1

class Solution(object):
    def TrackBack(self, trace, start, end):
        augmentingPath=[]
        currentNode=end
        e = trace[currentNode]
        while not (e.v1==0 and e.v2==0):
            augmentingPath.append(e)
            currentNode=e.GetAnotherVertex(currentNode)
            e = trace[currentNode]
        return augmentingPath
               
    def FindAugmentingPath(self, flowGraph, source, target, n):
        visited=[0]*(n+1)
        trace=[None]*(n+1)
        dummyEdge=Edge(0,0,999999)
        queue=[(source, dummyEdge)]

        while len(queue) > 0:
            currentVertex,fromEdge=queue.pop(0)
            if 1==visited[currentVertex]:
                continue
            visited[currentVertex]=1
            trace[currentVertex]=fromEdge            
            if currentVertex==target: #TODO: add flow to maxFlow #
                return self.TrackBack(trace, source, target)
            #TODO: add new vertexs to queue#
            for e in flowGraph[currentVertex]:
                if e.currentFlow < e.capacity and 0==visited[e.GetAnotherVertex(currentVertex)]:
                    queue.append((e.GetAnotherVertex(currentVertex),e))
        return None
    
    def UpdateFlowGraph(self, augmentingPath):
        eData=list(map(lambda e: e.capacity-e.currentFlow, augmentingPath))
        addableFlow=min(eData)
        for e in augmentingPath:
            e.currentFlow+=addableFlow
        return addableFlow
        
    def FordFulkerson(self, flowGraph, source, target, n):
        maxFlow=0
        while True:
            augmentingPath=self.FindAugmentingPath(flowGraph, source, target, n)
            if None==augmentingPath:
                break
            maxFlow+=self.UpdateFlowGraph(augmentingPath)
        return maxFlow
            
    def GetMaxInternetBandwidth(self, flowGraph, source, target, n):
        return self.FordFulkerson(flowGraph, source, target, n)  
        
case=0      
while True: 
    try:
        n = int(input())
        if 0==n:
            break
        fg={i:[] for i in range(n+1)}       
        src,trgt,edges = map(int, input().split())
        for r in range(edges):
            v1,v2,capacity = map(int, input().split())
            e=Edge(v1,v2,capacity)
            fg[v1].append(e)
            fg[v2].append(e)
    except:
        print("Input error!")
        break
    sln=Solution()
    maxFlow=sln.GetMaxInternetBandwidth(fg,src,trgt,n)
    case+=1
    print(f"Network {case}")
    print(f"The bandwidth is {maxFlow}.")
