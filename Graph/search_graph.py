import queue


# depth first search
# search a connected graph
class DFS:
    def __init__(self):
        self.marked = [] # if the vertex has been visited
        self.count = 0 # number of connected vertexes

    def __call__(self, G, s):
        for i in range(G.V):
            self.marked.append(False)
        self.dfs(G, s)

    def dfs(self, G, v):
        self.marked[v] = True
        self.count += 1
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)


# depth first path search
class DepthFirstPaths:
    def __init__(self):
        self.marked = []
        self.EdgeTo = []
        self.s = 0

    def __call__(self, G, s):
        self.s = s
        for i in range(G.V):
            self.marked.append(False)
            self.EdgeTo.append(i)
        self.dfs(G, s)

    def dfs(self, G, v):
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.EdgeTo[w] = v
                self.dfs(G, w)

    def hasPathTo(self, v):
        return self.marked[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
            print(str(v)+": no path")
        else:
            path_stack = []
            x = v
            while x is not self.s:
                path_stack.append(x)
                x = self.EdgeTo[x]
            path_stack.append(self.s)
            string = str(v)+': '
            for i in range(len(path_stack)):
                if i is len(path_stack)-1:
                    string += str(path_stack[-1-i])
                else:
                    string += str(path_stack[-1-i])
                    string += '-->'
            print(string)


# breadth first path search
class BreadthFirstPaths:
    def __init__(self):
        self.marked = []
        self.edgeTo = []
        self.s = 0

    def __call__(self, G, s):
        q = queue.Queue()
        self.s = s
        for i in range(G.V):
            self.marked.append(False)
            self.edgeTo.append(i)

        self.marked[s] = True
        q.put(s)
        while not q.empty():
            v = q.get()
            for w in G.adj[v]:
                if not self.marked[w]:
                    self.marked[w] = True
                    self.edgeTo[w] = v
                    q.put(w)

    def hasPathTo(self, v):
        return self.marked[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
            print(str(v)+": no path")
        else:
            path_stack = []
            x = v
            while x is not self.s:
                path_stack.append(x)
                x = self.edgeTo[x]
            path_stack.append(self.s)
            string = str(v)+': '
            for i in range(len(path_stack)):
                if i is len(path_stack)-1:
                    string += str(path_stack[-1-i])
                else:
                    string += str(path_stack[-1-i])
                    string += '-->'
            print(string)



if __name__ == '__main__':
    import graph
    graph = graph.Graph('./tinyG.txt')
    graph.print()

    # DFS
    print('DFS test: ')
    search = DFS()
    search(graph, 0)
    print('Vertexes visited:\n')
    for i in range(graph.V):
        print(search.marked[i])
    print('Count of connected vertexes')
    print(search.count)

    # depth first path search
    print('Depth first path search:')
    dfp = DepthFirstPaths()
    dfp(graph, 0)
    for v in range(graph.V):
        dfp.pathTo(v)

    # breadth first path search
    print('Breadth first path search:')
    bfp = BreadthFirstPaths()
    bfp(graph, 0)
    for v in range(graph.V):
        bfp.pathTo(v)