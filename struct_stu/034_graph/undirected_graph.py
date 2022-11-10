import  queue

# 无向图的广搜与深搜
class UndirectedGraph:
    
    def __init__(self, vertex_num):
        self.found = False
        
        self.vertex_num = vertex_num
        self.adj = []
        
        for i in range(vertex_num):
            self.adj.append([])
    
    def add_edge(self, s, t):
        self.adj[s].append(t)
        self.adj[t].append(s)
        
    
    def print_graph(self):
        print(self.adj)
    
    def print_path(self, prev, s, t):
        if prev[t] != -1 and t != s:
            self.print_path(prev, s, prev[t])
        print(t, end=" ")
    
    def bfs(self, s, t):
        if s == t:
            return
        
        visited = [False] * self.vertex_num
        visited[s] = True
        
        queue_fifo = queue.Queue()
        queue_fifo.put(s)
        prev = [-1] * self.vertex_num
        
        while queue_fifo.empty() is False:
            w = queue_fifo.get()
            for i in range(len(self.adj[w])):
                q = self.adj[w][i]
                if visited[q] is False:
                    prev[q] = w
                    if q == t:
                        self.print_path(prev, s, t)
                        return
                    visited[q] = True
                    queue_fifo.put(q)
    
    def dfs(self, s, t):
        visited = [False] * self.vertex_num
        visited[s] = True
        
        prev = [-1] * self.vertex_num
        
        self.recursive_dfs(s, t, visited, prev)
        self.print_path(prev, s, t)
        
    def recursive_dfs(self, w, t, visited, prev):
        if self.found is True:
            return
        visited[w] = True
        if w == t:
            self.found = True
            return
        
        for i in range(len(self.adj[w])):
            q = self.adj[w][i]
            if visited[q] is False:
                prev[q] = w
                self.recursive_dfs(q, t, visited, prev)
    



if __name__ == '__main__':
    undirectedGraph = UndirectedGraph(8)
    undirectedGraph.add_edge(0, 1)
    undirectedGraph.add_edge(0, 3)
    undirectedGraph.add_edge(1, 2)
    undirectedGraph.add_edge(1, 4)
    undirectedGraph.add_edge(2, 5)
    undirectedGraph.add_edge(3, 4)
    undirectedGraph.add_edge(4, 5)
    undirectedGraph.add_edge(4, 6)
    undirectedGraph.add_edge(5, 7)
    undirectedGraph.add_edge(6, 7)
    undirectedGraph.print_graph()
    
    undirectedGraph.dfs(0, 7)
