import networkx as nx
import matplotlib.pyplot as plt
import math
from queue import PriorityQueue
import copy as cp
from haversine import haversine, Unit

def build_graph(vis=False):
    G = nx.Graph()
    G.add_node("1", pos = (0,0))
    G.add_node("2", pos = (0,2))
    G.add_node("3", pos = (1,2))
    G.add_node("4", pos = (-2,0))
    
    G.add_edge("1","2", weight=2)
    G.add_edge("2","3", weight=1)
    G.add_edge("3","4", weight=5)
    G.add_edge("1","4", weight=2)

    if vis:
        #plt.subplot(121)
        pos= nx.get_node_attributes(G,'pos')#nx.spring_layout(G) # pos = nx.nx_agraph.graphviz_layout(G)
        nx.draw_networkx(G,pos)
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        plt.show()
    return G

def astar(G, start_node, end_node):
    """
    Output:
    list containing the nddes to take to the destination: [1, 2, 3]
    output runlist: [(set(), [1]), ({1}, [2, 4]), ({1, 2}, [4, 3]), ({1, 2, 4}, [3])]
    list containing the visited nbodes at each step as well as the ones that are candidates for exploring! stored as a list of tuples that conatin a set and a list
    """
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
            
    run_list = []
    # Initilize the starting node into visited
    p_queue = PriorityQueue()
    visited = set()
    prev_map = dict()
    p_queue.put((heuristic(G,start_node, end_node), start_node))

    while not p_queue.empty():
        ## Addd stuff into plotting dict
        run_list.append(((cp.copy(visited)), cp.copy([b for (a,b) in p_queue.queue])))

        short = p_queue.get()
        node = short[1]
        node_pri = short[0]
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
    return (min_path, run_list)
  
def heuristic(g, cur_node, end_node):
    cur_pos = g.nodes()[cur_node]["pos"]
    end_pos = g.nodes()[end_node]["pos"]
    dx = abs(cur_pos[0]-end_pos[0])
    dy = abs(cur_pos[1]-end_pos[1])
    dist = math.sqrt(dx*dx+dy*dy)

    #cur_pos = g.nodes()[cur_node]["coords"]
    #end_pos = g.nodes()[end_node]["coords"]
    ## Use coordinates to calulate distance
    #dist = haversine(cur_pos, end_pos, unit='ft')
    return dist


def plot_video(G, run_data):
    ## Do setup of stuff here
    frame_num = 0
    ## Loop through each state of ASTAR
    for frame in run_data:
        # Process this into a mtaplotlib call
        build_matplotlib(G, run_data, frame_num)
        frame_num += 1

    # Call ffmpeg to make a video
    # import os
    # import imageio

    # png_dir = '../animation/png'
    # images = []
    # for file_name in sorted(os.listdir(png_dir)):
    #     if file_name.endswith('.png'):
    #         file_path = os.path.join(png_dir, file_name)
    #         images.append(imageio.imread(file_path))
    # imageio.mimsave('../animation/gif/movie.gif', images)

def build_matplotlib(G, astar_data, frame_num):
    visited = astar_data[0] # This is a set of visited nodes
    in_queue = astar_data[1] # List of nodes in pqueue in order!

    for node in G.nodes():
        # Do some plotting
        pass
    for vist_node in visited:
        vist_node = G[vist_node]
        # Plot operation
    for explore_node in in_queue:
        explore_node = G[explore_node]
        #plot operation
    
    plt.savefig("images/file%02d.png" % frame_num)


def route_find():
    pass


if __name__ == "__main__":
    graph = build_graph(False)
    ret = astar(graph, "1", "3")
    print(ret[0])
    print(ret[1])