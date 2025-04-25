import math

class CirculantGraph:
    def __init__(self, n):
        self.L = [1, 2, 3, 4]
        self.edges = {}
        #n = 5
        self.r = n - 3 #2
        self.diff = n - self.r #3
        self.fact = math.floor(self.diff/2) #1
        self.circulant(n)


    def edgeWeight(self, t, n):
        for i in range(0, (t - self.fact -1)):
            for j in range((self.fact + i + 1), t):
                if(i <= self.fact) and (j >= (n - self.fact + i)):
                    self.edges[f'{{{i+1},{j}}}'] = None
                else:
                    self.edges[f'{{{i+1},{j}}}'] = self.L[i] + self.L[j]


    def duplicate(self, t):
        for i in range(1, (t - self.fact - 2)):
            for j in range((self.fact + i + 1), (t-1)):
                for l in range(0, (i-1)):
                    for w in range((j+1), t):
                        if (self.edges[f'{{{l+1},{w}}}'] != None) and (self.edges[f'{{{i},{j}}}'] == self.edges[f'{{{l+1},{w}}}']):
                            return True
        return False

    def find_vertices(self, n):
        if (n < 5) or (n > 10):
            raise ValueError('Values m and n must be greater than or equal to 2 and less than or equal to 10')
        else:
            t = 5
            m = 4
            while (t <= n):
                self.L.append(m+1)
                self.edgeWeight(t, n)
                if self.duplicate(t) == False:
                    t = t+1
                    m = m+1


    def find_edges(self, i, j, k):
        #create a list containing the current vertex and offset 1 around
        adjacencies = self.L.copy()
        offset = [i, j, k]
        for i in offset:
            adjacencies.remove(i)
        return adjacencies


    def find_weight(self, vertex, current):
        if (f'{{{vertex},{current}}}') in self.edges:
            pass
        else:
            self.edges[f'{{{current},{vertex}}}'] = 1


    def add_edges(self, n):
        for i in range (0, len(self.L)):
            current = self.L[i]
            if i == 0:
                adjacencies = self.find_edges(self.L[i], self.L[i+1], self.L[-1])
                for vertex in adjacencies:
                    self.find_weight(vertex, current)
            elif i == len(self.L) - 1:
                adjacencies = self.find_edges(self.L[i], self.L[0], self.L[i-1])
                for vertex in adjacencies:
                    self.find_weight(vertex, current)
            else:
                adjacencies = self.find_edges(self.L[i], self.L[i+1], self.L[i-1])
                for vertex in adjacencies:
                    self.find_weight(vertex, current)


    def display(self):
        print('Vertices: ', self.L)
        print('Edges and Weights: ')
        for vertex, neighbors in self.edges.items():
            print(f'{vertex}: {neighbors}')


    def circulant(self, n):
        self.add_edges(n)
        self.find_vertices(n)
        self.display()

CirculantGraph(5)