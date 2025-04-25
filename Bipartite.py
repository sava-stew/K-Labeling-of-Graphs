class BipartiteGraph:
    def __init__(self, m, n):
        self.U = [None] * m
        self.V = [None] * n
        self.edges = {}
        self.bipartite(m, n)

    def add_vertices(self, m, n):
        if ((m or n) < 2) or ((m or n) > 10):
            raise ValueError('Values m and n must be greater than or equal to 2 and less than or equal to 10')
        else:
            #adjustments on i and j values were made from provided algorithm due to indexing in Python
            if (n % 2 == 0):
                for i in range (0, m):
                    self.U[i] = ((n*i) // 2) + 1
                for j in range (0, (n//2)):
                    self.V[j] = j + 1
                for j in range((n//2), n):
                    self.V[j] = (n * (m-1)) // 2 + j + 1
            if ((n % 2 == 1) and (m % 2 == 0)):
                for i in range(0, m//2):
                    self.U[i] = i + 1
                for i in range((m//2), m):
                    self.U[i] = (m * (n-1)) // 2 + i + 1
                for j in range(0, n):
                    self.V[j] = (m*j) // 2 + 1
            if ((n % 2 == 1) and (m % 2 == 1)):
                for i in range(0, m):
                    self.U[i] = (i * (n+1)) // 2 + 1
                for j in range (0, (n+1) // 2):
                     self.V[j] = j + 1
                for j in range((n+1) // 2, n):
                    self.V[j] = ((n+1) * (m-1) // 2) + j + 1

    def add_edges(self):
        for u in self.U:
            for v in self.V:
                self.edges[f'{{{u},{v}}}'] = u + v

    def display(self):
        print('Set U: ', self.U)
        print('Set V: ', self.V)
        print('Edges and Weights: ')
        for edge, weight in self.edges.items():
            print(f'{edge}: {weight}')

    def bipartite(self, m, n):
        self.add_vertices(m, n)
        self.add_edges()
        self.display()