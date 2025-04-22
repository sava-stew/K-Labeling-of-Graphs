class MongolianTentGraph:
    def __init__(self, n):
        self.path1 = set()
        self.path2 = set()
        self.z = set()
        self.path1Edges = {}
        self.path2Edges = {}
        self.zEdges = {}
        self.mongolianTent(n)


    def add_vertices(self, m):
        if (n < 2) or (n > 10):
            raise ValueError('Values m and n must be greater than or equal to 2 and less than or equal to 10')
        else:
            for i in range(1, n+1):
                self.path1.add(i)
                self.path1Edges[i] = []
                self.path2.add(i)
                self.path2Edges[i] = []


    def addPaths(self):
        #Paths will have same order and size, as they are part of a mongolian tent graph
        for i in self.path1:
            if i == 1:
                self.path1Edges[i].append(i+1)
                self.path2Edges[i].append(i+1)
            elif i == (len(self.path1Edges)):
                self.path1Edges[i].append(i-1)
                self.path2Edges[i].append(i-1)
            else:
                self.path1Edges[i].append(i-1)
                self.path1Edges[i].append(i+1)
                self.path2Edges[i].append(i-1)
                self.path2Edges[i].append(i+1)


    def addLadder(self):
        for i in self.path1:
            self.path1Edges[i].append(i)
            self.path2Edges[i].append(i)


    def addTent(self):
        z = len(self.path1)+1
        self.z.add(z)
        self.zEdges[z] = []
        for i in self.path1:
            self.path1Edges[i].append(z)
            self.zEdges[z].append(i)

    def display(self):
        print('Path 1 Vertices: ', self.path1)
        print('Path 2 Vertices: ', self.path2)
        print('Path 1 Adjacencies: ')
        for vertex, neighbors in self.path1Edges.items():
            print(f'{vertex}: {neighbors}')
        print('Path 2 Adjacencies: ')
        for vertex, neighbors in self.path2Edges.items():
            print(f'{vertex}: {neighbors}')
        if len(self.z) != 0:
            print('Z: ', self.z)
            print('Z Adjacencies:')
            for vertex, neighbors in self.zEdges.items():
                print(f'{vertex}: {neighbors}')
        else:
            print('\n')


    def mongolianTent(self, m):
        self.add_vertices(m)

        self.addPaths()
        print('---Path Graph Info---')
        self.display()

        self.addLadder()
        print('---Ladder Graph Info---')
        self.display()

        self.addTent()
        print('---Mongolian Tent Graph Info---')
        self.display()
