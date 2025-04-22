class BipartiteGraph:
    def __init__(self, m, n):
        self.U = set()
        self.V = set()
        self.UEdges = {}
        self.VEdges = {}
        self.bipartite(m, n)


    def add_vertices(self, m, n):
        if ((m or n) < 2) or ((m or n) > 10):
            raise ValueError('Values m and n must be greater than or equal to 2 and less than or equal to 10')
        else:
            for i in range(1, m+1):
                self.U.add(i)
                self.UEdges[i] = []
            for i in range(1, n+1):
                self.V.add(i)
                self.VEdges[i] = []


    def add_edges(self):
        for u in self.U:
            for v in self.V:
                self.UEdges[u].append(v)

        for v in self.V:
            for u in self.U:
                self.VEdges[v].append(u)


    def display(self):
        print('Set U: ', self.U)
        print('Set V: ', self.V)
        print('Set U Adjacency List: ')
        for vertex, neighbors in self.UEdges.items():
            print(f'{vertex}: {neighbors}')
        print('Set V Adjacency List: ')
        for vertex, neighbors in self.VEdges.items():
            print(f'{vertex}: {neighbors}')


    def bipartite(self, m, n):
        self.add_vertices(m, n)
        self.add_edges()
        self.display()