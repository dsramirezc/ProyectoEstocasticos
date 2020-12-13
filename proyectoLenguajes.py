import numpy
from numpy.random import uniform as rand
import plotly.graph_objects as go
class RandomGraph:
    nodes=0
    edges=0
    roots=[]
    nroots=0
    alpha=0
    probability=0;
    adjacency=[]
    vis=[]
    num=[]
    low=[]
    articulationPoints=[]
    bridges=[]
    time=1
    root=0
    maxDepth=0
    isRoot=[]
    rootConnections=[]
    def __init__(self, nodes, alpha,nroots ):
        self.nroots=nroots
        self.edges =0
        self.nodes = nodes
        self.probability = pow(nodes,-alpha)
        self.adjacency=[[] for i in range(nodes)]
        self.alpha =alpha
        self.isRoot=[False for i in range(nodes)]
        self.roots=[i for   i in range(nodes)]
        self.rootConnections=[0 for   i in range(nodes)]
        numpy.random.shuffle(self.roots)
        numpy.random.shuffle(self.roots)
        numpy.random.shuffle(self.roots)
        self.roots=self.roots[0:self.nroots]
        for i in self.roots:
            isRoot[i]=True
        self.vis=[False for i in range(nodes)]
        self.num=[0 for i in range(nodes)]
        self.low=[0 for i in range(nodes)]
        for i in range(nodes):
            for j in range(nodes):
                if i==j:
                    continue
                if rand()<=self.probability:
                    self.adjacency[i].append(j)
                    self.edges+=1
        self.getArticulationPointsAndBridges(self.root,-1)
        self.getMaxDepth()
    def reconstruct(self):
        self.tim=1
        self.bridges=[]
        self.articulationPoints=[]
        self.rootConnections=[0 for i in range(nodes)]
        self.roots=[i for   i in range(self.nodes)]
        numpy.random.shuffle(self.roots)
        numpy.random.shuffle(self.roots)
        numpy.random.shuffle(self.roots)
        self.roots=self.roots[0:self.nroots]
        for i in self.roots:
            isRoot[i]=True
        self.adjacency=[[] for i in range(self.nodes)]
        self.vis=[False for i in range(self.nodes)]
        self.num=[0 for i in range(self.nodes)]
        self.low=[0 for i in range(self.nodes)]
        for i in range(self.nodes):
            for j in range(self.nodes):
                if i==j:
                    continue
                if rand()<=self.probability:
                    self.adjacency[i].append(j)
                    self.edges+=1
        self.getArticulationPointsAndBridges(self.root,-1)
        self.getMaxDepth()
        
    def isDisperse(self):
        return (self.nodes-self.edges*self.alpha)>=0
    def isDense(self):
        return (self.nodes-self.edges*self.alpha)<0
    def printEdges(self):
        for i in range(self.nodes):
            for j in self.adjacency[i]:
                print(i,j)
    def getArticulationPointsAndBridges(self,node,parent):
        self.vis[node]=True
        self.num[node]=self.time
        self.time+=1
        self.low[node]=self.num[node]
        cnt=0
        flag=False
        for i in self.adjacency[node]:
            if i==parent:
                continue
            if self.vis[i]:
                self.low[node]=min(self.low[node],self.num[i]);
                continue
            self.getArticulationPointsAndBridges(i,node)
            self.low[node]=min(self.low[node],self.low[i])
            if self.num[node]<=self.low[i]:
                flag=True
            if self.num[node]<self.low[i]:
                self.bridges.append([min(node,i),max(node,i)]);
            cnt+=1
        if((self.root==node and cnt>1) or (self.root!=node and flag)):
            self.articulationPoints.append(node)
    def getMaxDepth(self):
        depth=0
        bfs=self.roots.copy()
        auxVis=[False for i in range(self.nodes)]
        while len(bfs)>0:
            depth+=1
            for i in bfs:
                auxVis[i]=True
            bfs1=[]
            for i in bfs:
                for j in self.adjacency[i]:
                    if not auxVis[j]:
                        bfs1.append(j)
            bfs=bfs1.copy()
        self.maxDepth=depth

                
            
    
