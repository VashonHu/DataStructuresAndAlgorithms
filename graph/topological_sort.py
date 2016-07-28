from DFS import topoList, DFS

def topoSort(g):
    DFS(g)
    return topoList.reverse()