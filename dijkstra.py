import sys
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex \tJarak Dari Node Asal")
        for node in range(self.V):
            print(node, "\t", dist[node])

    #fungsi untuk mencari vertex dengan jarak terpendek yang
    #tidak ada di sptSet
    def minDistance(self, dist, sptSet):
 
        # Inisialisasi jarak minimum untuk node berikutnya
        min = sys.maxsize
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
        return min_index
    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for cout in range(self.V):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                dist[y] > dist[x] + self.graph[x][y]:
                        dist[y] = dist[x] + self.graph[x][y]
        self.printSolution(dist)

g = Graph(6)
g.graph = [[0, 80, 450, 0, 0, 0, 0],
        [80, 0, 0, 1600, 0, 0, 0],
        [450, 0, 0, 0, 2200, 0, 0],
        [0, 1600, 0, 0, 0, 800, 0],
        [0, 0, 2200, 0, 0, 0, 130],
        [0, 0, 0, 800, 0, 0, 0],
        [0, 0, 0, 0, 130, 130, 0]
        ];
 
g.dijkstra(0);