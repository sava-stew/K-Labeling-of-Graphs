class MongolianTentGraph:
    def __init__(self, n):
        self.path1 = [None] * (n+1)
        self.path2 = [None] * n
        self.z = 1
        self.path1[0] = self.z
        self.edges = {}
        self.mongolianTent(n)


    def add_vertices(self, n):
        if (n < 2) or (n > 10):
            raise ValueError('Values m and n must be greater than or equal to 2 and less than or equal to 10')
        else:
            for i in range(1, n+1):
                self.path1[i] = 2 * i
            self.path2[0] = self.path1[1]
            self.path2[1] = self.path1[n] + 1
            if n <= 2:
                return
            else:
                self.path2[n-1] = self.path1[n]
                for i in range (2, (n-1)):
                    self.path2[i] = self.path2[i-1] + 2


    def addEdges(self):
        #Paths will have same order and size, as they are part of a mongolian tent graph
        p1 = self.path1[1:]
        for i in range(0, len(p1)):
            #for each vertex in path1[1:n], add edge from vertex to z
            self.edges[f'{{{self.z},{p1[i]}}}'] = self.z + p1[i]
            #if last vertex in path1
            if i == len(p1)-1:
                #add edge from last vertex in path1 to last vertex in path2
                self.edges[f'{{{p1[i]},{self.path2[i]}}}'] = p1[i] + self.path2[i]
            else:
                #add edge from current vertex to next vertex in path1
                self.edges[f'{{{p1[i]},{p1[i+1]}}}'] = p1[i] + p1[i+1]
                #add edge from current vertex to corresponding vertex in path2
                self.edges[f'{{{p1[i]},{self.path2[i]}}}'] = p1[i] + self.path2[i]
                #add edge from corresponding vertex in path2 to next vertex in path2
                self.edges[f'{{{self.path2[i]},{self.path2[i+1]}}}'] = self.path2[i] + self.path2[i+1]


    def display(self):
        print('Z: ', self.path1[0])
        p1 = self.path1[1:]
        print('Vertices: ', self.path1, self.path2)
        print('Edges and Weights: ')
        for edge, weight in self.edges.items():
            print(f'{edge}: {weight}')


    def mongolianTent(self, m):
        self.add_vertices(m)
        self.addEdges()
        self.display()
