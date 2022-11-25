from collections import deque, namedtuple

Edge = namedtuple ('Edge', 'start, end, cost')
def create_edge(start, end, cost):
    return Edge(start, end, cost)

class Graph:
    def __init__(self, edges):
        self.edges = [create_edge(*e) for e in edges]

    def vertices(self):
        return set(
            e.start for e in self.edges
        ).union(e.end for e in self.edges)

    # Algorithm
    def get_neighbour(self, v):
        neighbours = []
        for e in self.edges:
            if e.start == v:
                neighbours.append((e.end, e.cost))

        return neighbours

    def dijkstra(self, source, destination):
        distances = {v: float("inf") for v in self.vertices()}
        prev_v = {v: None for v in self.vertices()}

        distances[source] = 0
        vertices = list(self.vertices())[:]

        while len(vertices) > 0:
            v = min(vertices, key=lambda u: distances[u])
            vertices.remove(v)
            if distances[v] == float("inf"):
                break
            for neighbour, cost in self.get_neighbour(v):
                path_cost = distances[v] + cost
                if path_cost < distances[neighbour]:
                    distances[neighbour] = path_cost
                    prev_v[neighbour] = v

        path = []
        curr_v = destination
        while prev_v[curr_v] is not None:
            path.insert(0, curr_v)
            curr_v = prev_v[curr_v]
        path.insert(0, curr_v)

        return path

def get_shortest_path(start, end):
    if __name__ == "__main__":
        graph = Graph([
            ("1", "3", 1),("1", "4", 1),("3", "2", 1),
            ("2", "7", 1),("7", "8", 1),("3", "5", 1),
            ("5", "6", 1),("6", "2", 1),("4", "5", 1),
            ("4", "2", 1),("3", "1", 1),("2", "3", 1),
            ("8", "3", 1)
        ])

        route = graph.dijkstra(start, end)

        print(route)

start = "1"
end = "7"
get_shortest_path(start, end)
