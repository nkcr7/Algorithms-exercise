class Graph:
    def __init__(self, graph_path):
        self.V = 0
        self.E = 0
        self.adj = []
        with open(graph_path,'r') as file:
            self.V = int(file.readline())
            for i in range(self.V):
                self.adj.append([])

            self.E = int(file.readline())
            str = file.readline()
            while str:
                v = int(str.split(' ')[0])
                w = int(str.split(' ')[1].split('\n')[0])
                self.addEdge(v, w)
                str = file.readline()

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def print(self):
        print(self.adj)

# digraph
class Digraph:
    def __init__(self, graph_path=None):
        self.V = 0
        self.E = 0
        self.adj = []
        if graph_path is not None:
            with open(graph_path,'r') as file:
                self.V = int(file.readline())
                for i in range(self.V):
                    self.adj.append([])

                self.E = int(file.readline())
                str = file.readline()
                while str:
                    v = int(str.split(' ')[0])
                    w = int(str.split(' ')[1].split('\n')[0])
                    self.addEdge(v, w)
                    str = file.readline()

    def addEdge(self, v, w):
        self.adj[v].append(w)

    def reverse(self):
        R = Digraph()
        for i in range(self.V):
            R.adj.append([])
        for v in range(self.V):
            for w in self.adj[v]:
                R.addEdge(w, v)
        return R

    def print(self):
        print(self.adj)


# weighted edges
class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def either(self):
        return self.v

    def other(self,vertex):
        if vertex == self.v: return self.w
        elif vertex == self.w: return self.v
        else: print('no vertex available')

    def compareTo(self, that):
        if self.weight < that.weight: return -1
        elif self.weight > that.weight: return 1
        else: return 0

    def print(self):
        print('%d--%d: %.2f'%(self.v, self.w, self.weight))


# weighted graph
class EdgeWeightedGraph:
    def __init__(self, graph_path):
        self.V = 0
        self.E = 0
        self.adj = []
        with open(graph_path, 'r') as file:
            self.V = int(file.readline())
            for i in range(self.V):
                self.adj.append([])

            self.E = int(file.readline())
            str = file.readline()
            while str:
                v = int(str.split(' ')[0])
                w = int(str.split(' ')[1])
                weight = float(str.split(' ')[2].split('\n')[0])
                edge = Edge(v, w, weight)
                self.addEdge(edge)
                str = file.readline()

    def addEdge(self, edge):
        v = edge.either()
        w = edge.other(v)
        self.adj[v].append(edge)
        self.adj[w].append(edge)

    def print(self):
        for v in range(self.V):
            for e in self.adj[v]:
                if e.other(v) > v: # only print one representation. one edge has two copies in the graph
                    print('%d--%d: %.2f'%(v, e.other(v), e.weight))





if __name__=='__main__':

    print('Graph: ')
    graph = Graph('./tinyG.txt')
    graph.print()

    print('\n\nDigraph: ')
    digraph = Digraph('./tinyDG.txt')
    digraph.print()
    R = digraph.reverse()
    R.print()

    print('\n\nWeighted edge: ')
    edge1 = Edge(1,2,0.55)
    edge2 = Edge(2,3, 1.23)
    edge1.print()
    edge2.print()
    print(edge1.compareTo(edge2))

    print('\n\nEdge weighted graph: ')
    ewg = EdgeWeightedGraph('./tinyEWG.txt')
    ewg.print()