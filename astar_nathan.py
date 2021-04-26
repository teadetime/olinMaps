import networkx as nx
import matplotlib.pyplot as plt
import math
from queue import PriorityQueue

def build_graph(vis=False):
    G = nx.Graph()
    G.add_node(1, pos = (0,0))
    G.add_node(2, pos = (0,2))
    G.add_node(3, pos = (1,2))
    G.add_node(4, pos = (-2,0))
    
    G.add_edge(1,2, weight=2)
    G.add_edge(2,3, weight=1)
    G.add_edge(3,4, weight=5)
    G.add_edge(1,4, weight=2)

    if vis:
        #plt.subplot(121)
        pos= nx.get_node_attributes(G,'pos')#nx.spring_layout(G) # pos = nx.nx_agraph.graphviz_layout(G)
        nx.draw_networkx(G,pos)
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        plt.show()
    return G

def astar(G, start_node, end_node):
    #*******#
    #*Setup*#
    #*******#
    node_dict = dict()
    # nodes_list = [(node, math.inf if node != start_node) for node in list(G.nodes())]
    # for node in nodes_list:
    #     node_dict[node[0]] = node[1]
    
    for node in list(G.nodes()):
        if node == start_node:
            best_dist = 0
        else:
            best_dist = math.inf
        node_dict[node] = best_dist
            

    # Initilize the starting node into visited
    p_queue = PriorityQueue()
    visited = set()
    prev_map = dict()
    p_queue.put((heuristic(G,start_node, end_node), start_node))

    while not p_queue.empty():
        short = p_queue.get()
        node = short[1]
        node_pri = short[0]
        print(node)
        print(node_pri)
        if node == end_node: break
        visited.add(node)
        dist_to_node = node_dict[node] ## NOT SURE THIS IS RIGHT
        adj_list = G.adj[node]

        for other_node in adj_list:
            if other_node in visited: continue
            weight = G[node][other_node]['weight']
            new_dist = dist_to_node + weight

            if new_dist < node_dict[other_node]:
                node_dict[other_node] = new_dist
                prev_map[other_node] = node
                p_queue.put((new_dist + heuristic(G,start_node, end_node), other_node))

    if end_node not in prev_map:
        return []

    # Reconstruct the path from the previous vertex mapping dictionary
    min_path = [end_node]
    curr_vertex = end_node
    while curr_vertex != start_node:
        prev_vertex = prev_map[curr_vertex]
        min_path.append(prev_vertex)
        curr_vertex = prev_vertex
    min_path.reverse()
    return min_path
  
def heuristic(g, cur_node, end_node):
    cur_pos = g.nodes()[cur_node]["pos"]
    end_pos = g.nodes()[end_node]["pos"]
    dx = abs(cur_pos[0]-end_pos[0])
    dy = abs(cur_pos[1]-end_pos[1])
    return (dx+dy)

if __name__ == "__main__":
    graph = build_graph(False)
    print(astar(graph, 1, 3))