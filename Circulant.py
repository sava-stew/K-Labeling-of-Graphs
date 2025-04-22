class CirculantGraph:
    def __init__(self, n):
        self.U = set()
        self.UEdges = {}
        self.circulant(n)


    def add_vertices(self, n):
        if (n < 5) or (n > 10):
            raise ValueError('Values m and n must be greater than or equal to 2 and less than or equal to 10')
        else:
            for i in range(1, n+1):
                self.U.add(i)
                self.UEdges[i] = []


    def find_edges(self, i, j, k):
        #create set of vertex and the vertex left and right of original vertex
        remove = set()
        remove.add(i)
        remove.add(j)
        remove.add(k)
        #create set all vertices except original vertex and two next to it
        #these will be the vertices that the original vertex should share an edge with
        adjacencies = (self.U).difference(remove)
        return adjacencies


    def add_edges(self, n):
        for i in self.U:
            if i == 1:
                adjacencies = self.find_edges(i, i+1, (len(self.U)))
                for vertex in adjacencies:
                    self.UEdges[i].append(vertex)
            elif i == len(self.U):
                adjacencies = self.find_edges(i, 1, i-1)
                for vertex in adjacencies:
                    self.UEdges[i].append(vertex)
            else:
                adjacencies = self.find_edges(i, i+1, i-1)
                for vertex in adjacencies:
                    self.UEdges[i].append(vertex)


    def display(self):
        print('Set U: ', self.U)
        print('U Adjacency List: ')
        for vertex, neighbors in self.UEdges.items():
            print(f'{vertex}: {neighbors}')


    def circulant(self, n):
        self.add_vertices(n)
        self.add_edges(n)
        self.display()

