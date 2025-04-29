import math
from lib2to3.pytree import generate_matches

class CirculantGraph:
    def __init__(self, n):
        self.n = n
        self.S = [1]
        self.circulant(n)


    def generate_sequence(self, n):
        if (n < 5):
            raise ValueError('Value n must be greater than or equal to 5')
        else:
            #upper = min(math.ceil(n / 2), 4)
            upper = 4
            # seed with [1, 2, ..., upper]
            l = list(range(1, upper + 1))
            #   l[k] = l[k-1] + l[k-3]
            while len(l) < n:
                j = l[-1] + l[-3]
                l.append(j)
            return l


    def circulant_adjacency(self, n, jumps):
        """
        Build the n×n adjacency matrix A for Ci(n, S), where S = jumps.
        """
        A = [[False]*n for _ in range(n)]
        for i in range(n):
            for s in jumps:
                A[i][(i+s) % n] = True
                A[i][(i-s) % n] = True
        return A


    def print_sum_matrix(self, labels, adjacency):
        """
        Print an (n+1)x(n+1) grid:
          • Top header row:    blank, then each vertex label
          • Each data row i:   label_i, then for each j:
                –   0             if i == j
                –  'x'            if adjacency[i][j] is True
                –  label_i+label_j otherwise
        """
        n = len(labels)
        # Header
        header = ["    "] + [f"{lbl:4}" for lbl in labels]
        print("Vertex Labels: ", labels)
        print("\nMatrix weight of edges: ")
        print("".join(header))
        # Body
        for i, li in enumerate(labels):
            row = [f"{li:4}"]
            for j, lj in enumerate(labels):
                if i == j:
                    row.append(f"{0:4}")
                elif adjacency[i][j]:
                    row.append("   x")
                else:
                    row.append(f"{li+lj:4}")
            print("".join(row))


    def circulant(self, n):
        labels = self.generate_sequence(n)
        A = self.circulant_adjacency(n, self.S)
        self.print_sum_matrix(labels, A)