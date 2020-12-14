import numpy
from numpy.random import uniform as rand
import random
import plotly.graph_objects as go

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
            for j in range(nodes):
                if i == j:
                    continue
                if rand() <= self.probability:
                    self.adjacency[i].append(j)
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
            for j in range(self.nodes):
                if i == j:
                    continue
                if rand() <= self.probability:
                    self.adjacency[i].append(j)
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
    def colorgraph(self):
        for i in range(self.nodes):
            self.posx.append(random.randint(0,1000))
            self.posy.append(random.randint(0,1000))
        edge_x = []
        edge_y = []
        for edge in range(self.nodes):
            x0 = self.posx[edge]
            y0 = self.posy[edge]
            for ad in self.adjacency[edge]:
                x1 = self.posx[ad]
                y1 = self.posy[ad]
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

        node_x = []
        node_y = []
        for node in range(self.nodes):
            x = self.posx[node]
            y = self.posy[node]
            node_x.append(x)
            node_y.append(y)

        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                # colorscale options
                #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
                #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
                #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
                colorscale='YlGnBu',
                reversescale=True,
                color=[],
                size=10,
                colorbar=dict(
                    thickness=15,
                    title='Node Connections',
                    xanchor='left',
                    titleside='right'
                ),
                line_width=2))
        node_adjacencies = []
        # node_text = []
        # for node, adjacencies in enumerate(G.adjacency()):
        #     node_adjacencies.append(len(adjacencies[1]))
        #     node_text.append('# of connections: '+str(len(adjacencies[1])))

        # node_trace.marker.color = node_adjacencies
        # node_trace.text = node_text
        fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='<br>Network graph made with Python',
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
rg = RandomGraph(10,0.3,2)
rg.colorgraph()