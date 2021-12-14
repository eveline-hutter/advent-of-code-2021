import networkx as nx
import matplotlib.pyplot as plt

with open('input12.txt') as file: puzzle_input = file.read().splitlines()    # open without /n

paths = [[line.split('-')[0], line.split('-')[1]] for line in puzzle_input]
graph = nx.Graph()
for path in paths:
    for node in path:
        if not graph.nodes.__contains__(node):
            cave_type = 'big_cave' if node.isupper() else 'small_cave'
            graph.add_node(node, type=cave_type)
    graph.add_edge(path[0], path[1], type='connects')
nx.draw(graph, with_labels=True)
plt.show()


def puzzle1():
    def find_all_paths(current, start, end, visited):
        if current == end:
            return 1

        no_of_paths = 0
        connected_caves = graph[current]
        for cave in connected_caves:
            if graph.nodes[cave]['type'] != 'small_cave' or cave not in visited:
                no_of_paths += find_all_paths(cave, start, end, visited | {cave})
        return no_of_paths

    print(find_all_paths('start', 'start', 'end', {'start'}))


def puzzle2():
    def find_all_paths(current, start, end, visited, second_visit):
        if current == end:
            return 1

        no_of_paths = 0
        connected_caves = graph[current]
        for cave in connected_caves:
            if graph.nodes[cave]['type'] != 'small_cave' or cave not in visited:
                no_of_paths += find_all_paths(cave, start, end, visited + [cave], second_visit)
            elif not second_visit and (cave != 'start' and cave != 'end'):
                no_of_paths += find_all_paths(cave, start, end, visited + [cave], True)
        return no_of_paths

    print(find_all_paths('start', 'start', 'end', ['start'], False))


puzzle1()
puzzle2()
