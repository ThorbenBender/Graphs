import unittest


class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, item):
        self.storage.append(item)

    def dequeue(self):
        item = self.storage[0]
        print('item', item)
        self.storage.pop(0)
        return item


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edges(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Sorry, couldn't find vertex")

    def bft(self, child):
        q = Queue()
        q.enqueue(child)
        visited = set()
        while len(q.storage) > 0:
            v = q.dequeue()

            if v not in visited:
                visited.add(v)
                for next_node in self.vertices[v]:
                    if next_node != set():
                        q.enqueue(next_node)

        return visited


        # if child not in visited:
        #     # print('child', child)
        #     anything.append(child)
        #     print('anything', anything)
        #     visited.add(child)
        #     for i in range(1, len(self.vertices) - 1):
        #         if child in self.vertices[i]:
        #             parent = self.vertices.keys([i])
        #             print('parent', parent)
        # for next_node in self.vertices[child]:
        #     self.dft(next_node)
test = [
    [1, 3],
    [2, 3],
    [3, 6],
    [5, 6],
    [5, 7],
    [4, 5],
    [4, 8],
    [8, 9],
    [11, 8],
    [10, 1]]

# graph = Graph()

test_set = set()

for t in test:
    test_set.add(t[1])
    test_set.add(t[0])
#     # graph.add_vertex(t[0])
#     # graph.add_vertex(t[1])
#     # graph.add_edges(t[0], t[1])


# for t in test_set:
#     graph.add_vertex(t)

# for v in test:
#     graph.add_edges(v[0], v[1])


def test_function(test, start):
    graph = Graph()

    test_set = set()

    for t in test:
        test_set.add(t[0])
        test_set.add(t[1])
        # graph.add_vertex(t[0])
        # graph.add_vertex(t[1])
        # graph.add_edges(t[0], t[1])

    for t in test_set:
        graph.add_vertex(t)

    for v in test:
        graph.add_edges(v[1], v[0])

    # print(graph.vertices)

    print("test", graph.bft(start))


# for q in test_set:
#     test_function(test, q)

test_function(test, 6)

# print("test none", graph.dft(6))
