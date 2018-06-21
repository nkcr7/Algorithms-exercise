import queue

# directed depth first search
class DirectedDFS:
    def __init__(self):
        self.marked = []
        self.s = []

    def __call__(self, G, s):
        if not isinstance(s, list):
            self.s = [s,]
        else:
            self.s = s
        for i in range(G.V):
            self.marked.append(False)

        for source in self.s:
            if not self.marked[source]:
                self.dfs(G, source)

    def dfs(self, G, v):
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)

    def print(self):
        string = ''
        for v in range(len(self.marked)):
            if self.marked[v] is True:
                string += str(v)
                string += ' '
        print(string)

    def reset(self):
        self.marked = []
        self.s = []


# depth first directed path search
class DepthFirstDirectedPaths:
    def __init__(self):
        self.marked = []
        self.s = 0
        self.edgeTo = []

    def __call__(self, G, s):
        self.s = s
        for i in range(G.V):
            self.marked.append(False)
            self.edgeTo.append(i)

        if not self.marked[s]:
            self.dfs(G, s)

    def dfs(self, G, v):
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)
                self.edgeTo[w] = v

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


# breadth first directed path search
class BreadthFirstDirectedPaths:
    def __init__(self):
        self.marked = []
        self.s = 0
        self.edgeTo = []

    def __call__(self, G, s):
        self.s = s
        for i in range(G.V):
            self.marked.append(False)
            self.edgeTo.append(i)

        q = queue.Queue()

        self.marked[s] = True
        q.put(s)
        while not q.empty():
            v = q.get()
            for w in G.adj[v]:
                if not self.marked[w]:
                    self.marked[w] = True
                    q.put(w)
                    self.edgeTo[w] = v

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


# search directed cycle
class DirectedCycle:
    def __init__(self):
        self.marked = []
        self.edgeTo = []
        self.onStack = []
        self.cycle = queue.LifoQueue() # stack

    def __call__(self, G):
        for i in range(G.V):
            self.marked.append(False)
            self.onStack.append(False)
            self.edgeTo.append(i)

        for s in range(G.V):
            if not self.marked[s]:
                self.dfs(G, s)

    def dfs(self, G, v):
        self.onStack[v] = True # enter the stack of function calls
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(G, w)
            elif self.onStack[w]: # find a cycle, revisit a node in the stack of function calls
                self.cycle.queue.clear()
                x = v
                while x != w:
                    self.cycle.put(x)
                    x = self.edgeTo[x]
                self.cycle.put(w)
                self.cycle.put(v)

        self.onStack[v] = False # leave the stack of function calls

    def print(self):
        if not self.cycle.empty():
            string = ''
            size = self.cycle.qsize()
            for i in range(size):
                string += str(self.cycle.get())
                if i != (size - 1):
                    string += '-->'
            print(string)


# depth first order
class DepthFirstOrder:
    def __init__(self):
        self.pre = queue.Queue()
        self.post = queue.Queue()
        self.reversePost = queue.LifoQueue()
        self.marked = []

    def __call__(self, G):
        for v in range(G.V):
            self.marked.append(False)
        for v in range(G.V):
            if not self.marked[v]:
                self.dfs(G, v)

    def dfs(self,G,v):
        self.pre.put(v)
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)
        self.post.put(v)
        self.reversePost.put(v)

    def getPre(self):
        return self.pre

    def getPost(self):
        return self.post

    def getReversePost(self):
        return self.reversePost

    def print(self):
        string = 'Pre order: \n'
        for i in range(self.pre.qsize()):
            string += str(self.pre.get())
            string += ' '
        print(string)

        string = 'Post order: \n'
        for i in range(self.post.qsize()):
            string += str(self.post.get())
            string += ' '
        print(string)

        string = 'Reverse post order: \n'
        for i in range(self.reversePost.qsize()):
            string += str(self.reversePost.get())
            string += ' '
        print(string)

# topological order, first check cycle, then depth first order
class Topological:
    def __call__(self, G):
        cyclefinder = DirectedCycle()
        cyclefinder(G)
        if cyclefinder.cycle.empty():
            dfo = DepthFirstOrder()
            dfo(G)
            self.order = dfo.getReversePost()

    def isDAG(self):
        return not self.order.empty()

    def print(self):
        string = ''
        for i in range(self.order.qsize()):
            string += str(self.order.get())
            string += ' '
        print(string)


if __name__ == '__main__':
    import graph
    print('DiGraph: ')
    digraph = graph.Digraph('./tinyDG.txt')
    digraph.print()

    # directed dfs
    ddfs = DirectedDFS()
    print('\n\nAccessable nodes: ')
    # source 1
    print('source: 1')
    ddfs(digraph, 1)
    ddfs.print()
    # source 2
    print('source: 2')
    ddfs.reset()
    ddfs(digraph, 2)
    ddfs.print()
    # source 1 2 6
    print('source: 1 2 6')
    ddfs.reset()
    ddfs(digraph, [1,2,6])
    ddfs.print()

    # depth first path search
    print('\n\nDepth first directed path search:')
    dfdp = DepthFirstDirectedPaths()
    dfdp(digraph, 0)
    for v in range(digraph.V):
        dfdp.pathTo(v)

    # breadth first path search
    print('\n\nBreadth first directed path search:')
    bfdp = BreadthFirstDirectedPaths()
    bfdp(digraph, 0)
    for v in range(digraph.V):
        bfdp.pathTo(v)


    # directed cycle
    print('\n\nDirected cycle search: ')
    dc = DirectedCycle()
    dc(digraph)
    dc.print()

    # depth first order
    print('\n\nDAG: ')
    dag = graph.Digraph('./tinyDAG.txt')
    dag.print()
    print('Depth first order: ')
    dfo = DepthFirstOrder()
    dfo(dag)
    dfo.print()

    # topological order
    print('\n\nTopological order: ')
    to = Topological()
    to(dag)
    to.print()