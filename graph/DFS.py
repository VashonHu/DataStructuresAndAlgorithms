from graph import GraphNode, GRAY, Graph, WHITE, BLACK

time = 0
topoList = []
def DFS(g):
    for n in g.travreseNode():
        n.f = 0
        if n.color == WHITE:
            DFS_visit(g, n)
def DFS_visit(g, n):
    global time
    n.color = GRAY
    time += 1
    n.d = time
    for v in n.adj:
        if v.color == WHITE:
            v.p = n
            DFS_visit(g, v)
    n.color = BLACK
    time += 1
    n.f = time
    global topoList
    topoList.append(n)


