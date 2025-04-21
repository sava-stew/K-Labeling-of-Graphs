class BipartiteGraph:
    def __init__(self):
        self.U = set()
        self.V = set()
        self.UEdges = {}
        self.VEdges = {}

    def add_vertices(self, m, n):
        if ((m or n) < 2) or ((m or n) > 10):
            raise ValueError('Values m and n must be greater than or equal to 2 and less than or equal to 10')
        else:
            for i in range(1, m+1):
                self.U.add(i)
                self.UEdges[i] = []
            for i in range(0, n):
                self.V.add(chr(i+65))
                self.VEdges[chr(i+65)] = []

    def add_edges(self):
        for u in self.U:
            for v in self.V:
                self.UEdges[u].append(v)

        for v in self.V:
            for u in self.U:
                self.VEdges[v].append(u)

    def display(self):
        print("Set U: ", self.U)
        print("Set V: ", self.V)
        print("U Adjacency List: ")
        for vertex, neighbors in self.UEdges.items():
            print(f"{vertex}: {neighbors}")
        print("V Adjacency List: ")
        for vertex, neighbors in self.VEdges.items():
            print(f"{vertex}: {neighbors}")

graph = BipartiteGraph()
m = int(input('Please enter the number of vertices for set U: '))
n = int(input('Please enter the number of vertices for set V: '))

graph.add_vertices(m, n)
graph.add_edges()

graph.display()
