import math

class CirculantGraph:
    def __init__(self, n):
        self.L = []
        self.edges = {}
        self.circulant(n)


    def add_vertices(self, n):
        if (n < 5) or (n > 10):
            raise ValueError('Values m and n must be greater than or equal to 2 and less than or equal to 10')
        else:
            upper = min(math.ceil(n/2), 4)
            for i in range(0, upper):
                self.L.append(i+1)
            if (n > 6):
                j = n - 1
            else:
                j = 1
            while (len(self.L) < n):
                self.L.append(j)
                j = j+(n-3)


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
            self.edges[f'{{{current},{vertex}}}'] = current + vertex


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
        self.add_vertices(n)
        self.add_edges(n)
        self.display()