"""
 1  function Dijkstra(Graph, source):
 2      for each vertex v in Graph:                                // Initializations
 3          dist[v] := infinity ;                                  // Unknown distance function from 
 4                                                                 // source to v
 5          previous[v] := undefined ;                             // Previous node in optimal path
 6      end for                                                    // from source
 7      
 8      dist[source] := 0 ;                                        // Distance from source to source
 9      Q := the set of all nodes in Graph ;                       // All nodes in the graph are
10                                                                 // unoptimized  thus are in Q
11      while Q is not empty:                                      // The main loop
12          u := vertex in Q with smallest distance in dist[] ;    // Source node in first case
13          remove u from Q ;
14          if dist[u] = infinity:
15              break ;                                            // all remaining vertices are
16          end if                                                 // inaccessible from source
17          
18          for each neighbor v of u:                              // where v has not yet been 
19                                                                 // removed from Q.
20              alt := dist[u] + dist_between(u, v) ;
21              if alt < dist[v]:                                  // Relax (u,v,a)
22                  dist[v] := alt ;
23                  previous[v] := u ;
24                  decrease-key v in Q;                           // Reorder v in the Queue
25              end if
26          end for
27      end while
28      return dist;
29  endfunction
"""

import sys


class Graph(object):
    def __init__(self, vertex_set=None):
        if vertex_set == None:
            vertex_set = []

        self.vertex_set = vertex_set

    def __str__(self):
        res = ""
        for v in self.vertex_set:
            res += v.__str__() + "\n"
        return res

    def dijkstra(self, info):
        for vertex in self.vertex_set:
            vertex.dist = sys.maxint

        src = get_vertex(info)

        if src:
            pass
        else:
            raise ValueError

    def add_vertex(self, info):
        for vertex in self.vertex_set:
            if vertex.info == info:
                return False

        self.vertex_set.append(Vertex(info))
        return True

    def get_vertex(self, info):
        for vertex in self.vertex_set:
            if (vertex.info == info):
                return vertex
        return None

    def remove_vertex(self, info):
        pass

    def add_edge(src, dest, weight):
        pass


class Vertex(object):
    def __init__(self, info):
        self.visited = False
        self.adj = []
        self.info = info
        self.dist = 0
        self.previous = None

    def __str__(self):
        return "Info: %10s\tVisited: %s" % (self.info, self.visited)

    def add_edge(self, dest, weight=0):
        self.adj.append(Edge(dest, weight))

    def remove_edge_to(self, dest):
        pass

    def get_info(self):
        return self.info


class Edge(object):
    def __init__(self, dest, weight=0):

        if not isinstance(dest, Vertex):
            raise TypeError

        self.dest = dest
        self.weight = weight

    def __str__(self):
        return "Dest: %s\tWeight: %s" % (self.dest.get_info(), self.weight)

    def get_weight(self):
        return self.weight

    def get_dest(self):
        return self.dest


g = Graph()

g.add_vertex('Porto')
g.add_vertex('Coimbra')
g.add_vertex('Lisboa')
g.add_vertex('Faro')
g.add_vertex('Braga')

print g