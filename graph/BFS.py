from graph import Graph, GraphNode, WHITE, GRAY, BLACK
import sys
from data_structure.queue import Queue

def BFS(g, s):
    s.color = GRAY
    s.d = 0
    s.p = None
    q = Queue()
    q.enqueue(s)
    while q.empty():
        u = q.dequeue()
        for v in u.adj:
            if v.color == WHITE:
                v.color = GRAY
                v.d = u.d + 1
                v.p = u
                q.enqueue(v)
        u.color = BLACK
