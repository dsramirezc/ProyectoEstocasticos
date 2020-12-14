import numpy
from numpy.random import uniform as rand
import random
import plotly.graph_objects as go
import plotly.express as px
class RandomGraph:
    # number of nodes
    nodes = 0
    # number of edge
    edges = 0
    # array of roots
    roots = []
    # number of roots
    nroots = 0
    # alpha parameter
    alpha = 0
    # probability of the grpah
    probability = 0
    # adjacency
    adjacency = []
    vis = []
    num = []
    low = []
    # nodes of brides
    articulationPoints = []
    # edge of bridge
    bridges = []
    time = 1
    root = 0
    maxDepth = 0
    isRoot = []
    rootConnections = []
    # graphpositions
    posx = []
    posy = []

    def __init__(self, nodes, alpha, nroots):
        self.nroots = nroots
        self.edges = 0
        self.nodes = nodes
        self.probability = pow(nodes, -alpha)
        self.adjacency = [[] for i in range(nodes)]
        self.alpha = alpha
        self.isRoot = [False for i in range(nodes)]
        self.roots = [i for i in range(nodes)]
        self.rootConnections = [0 for i in range(nodes)]
        numpy.random.shuffle(self.roots)
        numpy.random.shuffle(self.roots)
        numpy.random.shuffle(self.roots)
        self.roots = self.roots[0:self.nroots]
        for i in self.roots:
            self.isRoot[i] = True
        self.vis = [False for i in range(nodes)]
        self.num = [0 for i in range(nodes)]
        self.low = [0 for i in range(nodes)]
        for i in range(nodes):
            for j in range(i+1,nodes):
                if i == j:
                    continue
                if rand() <= self.probability:
                    self.adjacency[i].append(j)
                    self.adjacency[j].append(i)
                    self.edges += 1
        self.getArticulationPointsAndBridges(self.root, -1)
        self.getMaxDepth()
        self.posx = []
        self.posy = []

    def reconstruct(self):
        self.tim = 1
        self.bridges = []
        self.articulationPoints = []
        self.rootConnections = [0 for i in range(nodes)]
        self.roots = [i for i in range(self.nodes)]
        numpy.random.shuffle(self.roots)
        numpy.random.shuffle(self.roots)
        numpy.random.shuffle(self.roots)
        self.roots = self.roots[0:self.nroots]
        for i in self.roots:
            isRoot[i] = True
        self.adjacency = [[] for i in range(self.nodes)]
        self.vis = [False for i in range(self.nodes)]
        self.num = [0 for i in range(self.nodes)]
        self.low = [0 for i in range(self.nodes)]
        for i in range(self.nodes):
            for j in range(i+1,self.nodes):
                if i == j:
                    continue
                if rand() <= self.probability:
                    self.adjacency[i].append(j)
                    self.adjacency[j].append(i)
                    self.edges += 1
        self.getArticulationPointsAndBridges(self.root, -1)
        self.getMaxDepth()

    def isDisperse(self):
        return (self.nodes-self.edges*self.alpha) >= 0

    def isDense(self):
        return (self.nodes-self.edges*self.alpha) < 0

    def printEdges(self):
        for i in range(self.nodes):
            for j in self.adjacency[i]:
                print(i, j)

    def getArticulationPointsAndBridges(self, node, parent):
        self.vis[node] = True
        self.num[node] = self.time
        self.time += 1
        self.low[node] = self.num[node]
        cnt = 0
        flag = False
        for i in self.adjacency[node]:
            if i == parent:
                continue
            if self.vis[i]:
                self.low[node] = min(self.low[node], self.num[i])
                continue
            self.getArticulationPointsAndBridges(i, node)
            self.low[node] = min(self.low[node], self.low[i])
            if self.num[node] <= self.low[i]:
                flag = True
            if self.num[node] < self.low[i]:
                self.bridges.append([min(node, i), max(node, i)])
            cnt += 1
        if((self.root == node and cnt > 1) or (self.root != node and flag)):
            self.articulationPoints.append(node)

    def getMaxDepth(self):
        depth = 0
        bfs = self.roots.copy()
        auxVis = [False for i in range(self.nodes)]
        while len(bfs) > 0:
            depth += 1
            for i in bfs:
                auxVis[i] = True
            bfs1 = []
            for i in bfs:
                for j in self.adjacency[i]:
                    if not auxVis[j]:
                        bfs1.append(j)
            bfs = bfs1.copy()
        self.maxDepth = depth

    def checknotroot(self,ad,roots):
        for i in ad:
            if i in roots:
                return False
        return True
    def colorgraph(self):
        # colores
        colors = px.colors.qualitative.Safe
        for i in range(self.nodes):
            if(i in self.roots):
                self.posx.append(random.randint(100,900))
                self.posy.append(random.randint(700,1000))
            else:
                self.posx.append(random.randint(0,1000))
                self.posy.append(random.randint(0,500))
        edge_x = []
        edge_y = []
        edgecolors = []
        for edge in range(self.nodes):
            x0 = self.posx[edge]
            y0 = self.posy[edge]
            for ad in self.adjacency[edge]:
                x1 = self.posx[ad]
                y1 = self.posy[ad]
                edgecolors.append(colors[1])
                for b in self.bridges:
                    if(b[0] == edge and b[1]==ad):
                        edgecolors[len(edgecolors)-1]= colors[2]
                        break
                edge_x.append(x0)
                edge_x.append(x1)
                edge_x.append(None)
                edge_y.append(y0)
                edge_y.append(y1)
                edge_y.append(None)
        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines')
        # Color edge
        node_x = []
        node_y = []
        sizes = [100,50,10]
        for node in range(self.nodes):
            x = self.posx[node]
            y = self.posy[node]
            node_x.append(x)
            node_y.append(y)
        s = int(1000/self.nodes)
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            hoverinfo='text',
            marker=dict(
                # showscale=True,
                # colorscale options
                #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
                #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
                #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
                # colorscale='YlGnBu',
                # reversescale=True,
                color=[],
                size=s,
                line_width=2))
        # colors
        
        node_adjacencies = []
        node_text = []
        for i in range(self.nodes):
            nodetext =''
            if(i in self.roots):
                node_adjacencies.append(colors[4])
                nodetext = nodetext + "Servidor" + ' - '
            else:
                node_adjacencies.append(colors[0])
                nodetext = nodetext + "Cliente" + ' - '
            # no connection
            if(self.checknotroot(self.adjacency[i],self.roots) and i not in self.roots):
                node_adjacencies[i]=(colors[9])
            if(i in self.articulationPoints):
                node_adjacencies[i]=(colors[5])
            nodetext += 'Conexiones: '+str(len(self.adjacency[i])) + ' - ' + "Node #" + str(i)
            node_text.append(nodetext)
        node_trace.marker.color = node_adjacencies
        node_trace.text = node_text
        fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='Network Graph',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
            )
        fig.show()
# rg = RandomGraph(2,0.1,1)
# print(rg.adjacency)
# print(rg.roots)
# print(rg.bridges)
# rg.colorgraph()