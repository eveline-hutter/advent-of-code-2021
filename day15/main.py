import networkx as nx
import numpy as np

with open('input15.txt') as file: puzzle_input = [[int(no) for no in list(line)] for line in file.read().splitlines()]   # open without /n

cavern = np.array(puzzle_input)


def get_neighbours(cave, i, j):
    neighbours = []
    if i > 0: neighbours.append('' + str(i - 1) + '_' + str(j))  # top
    if i < len(cave) - 1: neighbours.append('' + str(i + 1) + '_' + str(j))  # bottom
    if j > 0: neighbours.append('' + str(i) + '_' + str(j - 1))  # left
    if j < len(cave[0]) - 1: neighbours.append('' + str(i) + '_' + str(j + 1))  # right
    return neighbours


def get_graph(cave):
    graph = nx.DiGraph()
    # add nodes to the graph
    for i in range(len(cave)):
        for j in range(len(cave[i])):
            node = '' + str(i) + '_' + str(j)
            graph.add_node(node, weight=cave[i][j])
    # add weighted edges to the graph where each edge weight is determined by the target node
    for i in range(len(cave)):
        for j in range(len(cave[i])):
            node = '' + str(i) + '_' + str(j)
            neighbours = get_neighbours(cave, i, j)
            [graph.add_edge(node, neighbour, weight=graph.nodes[neighbour]['weight']) for neighbour in neighbours]
    return graph


def scan_cave():
    cavern_size = len(cavern)
    cave = np.zeros((5 * cavern_size, 5 * cavern_size))
    # scan cave to the right
    next_cavern_to_the_right = np.array(cavern)
    cave[0:cavern_size, 0:cavern_size] += next_cavern_to_the_right
    for step in range(1, 5):
        next_cavern_to_the_right += 1
        for i in range(len(next_cavern_to_the_right)):
            for j in range(len(next_cavern_to_the_right[0])):
                if next_cavern_to_the_right[i][j] > 9: next_cavern_to_the_right[i][j] = 1
        cave[0:cavern_size, step * cavern_size: (step + 1) * cavern_size] += next_cavern_to_the_right
    # scan cave to the bottom
    next_cavern_to_the_bottom = np.array(cave[0:cavern_size, :])
    for step in range(1, 5):
        next_cavern_to_the_bottom += 1
        for i in range(len(next_cavern_to_the_bottom)):
            for j in range(len(next_cavern_to_the_bottom[0])):
                if next_cavern_to_the_bottom[i][j] > 9: next_cavern_to_the_bottom[i][j] = 1
        cave[step * cavern_size: (step + 1) * cavern_size, :] = next_cavern_to_the_bottom
    return cave


def puzzle1():
    graph = get_graph(cavern)
    start = '0_0'
    end = '' + str(len(cavern) - 1) + '_' + str(len(cavern[0]) - 1)
    lowest_risk_path = nx.single_source_dijkstra(graph, start, end)
    print(lowest_risk_path[0])


def puzzle2():
    cave = scan_cave()
    graph = get_graph(cave)
    start = '0_0'
    end = '' + str(len(cave) - 1) + '_' + str(len(cave[0]) - 1)
    lowest_risk_path = nx.single_source_dijkstra(graph, start, end)
    print(lowest_risk_path[0])


puzzle1()
puzzle2()
