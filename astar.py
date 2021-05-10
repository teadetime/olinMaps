import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
from queue import PriorityQueue
import copy as cp
from haversine import haversine, Unit
import csv

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
    p_queue = PriorityQueue() 
    visited = set()
    prev_map = dict()
    # Initilize the starting node into visited
    p_queue.put((heuristic(G,start_node, end_node), start_node))

    while not p_queue.empty():
        # Add stuff into plotting dict
        run_list.append(((cp.copy(visited)), cp.copy([b for (a,b) in p_queue.queue])))
        short = p_queue.get()
        node = short[1]
        node_pri = short[0]
        if node == end_node: break
        visited.add(node)
        dist_to_node = node_dict[node] # NOT SURE THIS IS RIGHT
        adj_list = G.adj[node]  # get adjacent nodes

        for other_node in adj_list:
            if other_node in visited: continue
            weight = G[node][other_node]['weight']
            new_dist = dist_to_node + weight

            if new_dist < node_dict[other_node]:
                node_dict[other_node] = new_dist
                prev_map[other_node] = node
                p_queue.put((new_dist + heuristic(G,other_node, end_node), other_node))
        
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
    # cur_pos = g.nodes()[cur_node]["pos"]
    # end_pos = g.nodes()[end_node]["pos"]
    # dx = abs(cur_pos[0]-end_pos[0])
    # dy = abs(cur_pos[1]-end_pos[1])
    # dist = math.sqrt(dx*dx+dy*dy)

    cur_pos = g.nodes()[cur_node]["coords"]
    end_pos = g.nodes()[end_node]["coords"]
    # Use coordinates to calulate distance
    dist = haversine(cur_pos, end_pos, unit='ft')
    return dist

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

def plot_video(G, run_data):
    ## Do setup of stuff here
    frame_num = 0
    ## Loop through each state of ASTAR
    for frame in run_data:
        # Process this into a mtaplotlib call
        build_matplotlib(G, run_data, frame_num)
        frame_num += 1

    # Call ffmpeg to make a video
    import os
    import imageio

    png_dir = '../animation/png'
    images = []
    for file_name in sorted(os.listdir(png_dir)):
        if file_name.endswith('.png'):
            file_path = os.path.join(png_dir, file_name)
            images.append(imageio.imread(file_path))
    imageio.mimsave('../animation/gif/movie.gif', images)


def add_dist_edge(graph, node1, node2, unit = "ft"):
    """
    Creates edges for nodes on the graph based on the distance between lat and long (haversine function)

    :param graph: networkx graph
    :param node1: Name of node
    :param node2:
    :param unit: unit for haversine calc
    """

    coords1 = graph.nodes()[node1]["coords"]
    coords2 = graph.nodes()[node2]["coords"]

    graph.add_edge(node1, node2, weight = round(haversine(coords1,coords2, unit=unit),1))
    
def build_graph(vis=False, csv_loc='node_connections.csv', csv_path_nodes ='path_nodes.csv', directed=False):
    """
    Creates a networkx graph G of useful locations at Olin with pixel and 
    longitude/latitude coordinates. The pathway attribute indicates whether or 
    not it should be displayed to the user during visualization.
    """
    if directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    G.add_node("AC 1",    pos=(324, 403),  coords = (42.29321996991126, -71.26459288853798), pathway=False)  #  AC 1
    G.add_node("AC 2",    pos=(456, 240),  coords = (42.29363418081095, -71.26422001841294), pathway=False)  # AC 2
    G.add_node("AC 3",    pos=(597, 137),  coords = (42.29386690104804, -71.2637380411814), pathway=False)   # AC 3
    G.add_node("AC 4",    pos=(404, 160),  coords = (42.29382686013987, -71.26440227411027), pathway=False)  # AC 4
    G.add_node("CC 1",    pos=(653, 376),  coords = (42.29328713953713, -71.26356098757215), pathway=False)  # CC 1
    G.add_node("CC 2",    pos=(717, 396),  coords = (42.29322457502598, -71.26333431385294), pathway=False)  # CC 2 (lower)
    G.add_node("CC 3",    pos=(758, 266),  coords = (42.29354657304486, -71.26318545348332), pathway=False)  # CC 3 (lower)
    G.add_node("CC 4",    pos=(636, 154),  coords = (42.29384938315572, -71.2636004581119), pathway=False)  # CC 4
    G.add_node("MH 1",    pos=(499, 488),  coords = (42.2930076842383, -71.26406733829359), pathway=False)  # MH 1
    G.add_node("MH 2",    pos=(582, 536),  coords = (42.29290340955621, -71.26378991671152), pathway=False)  # MH 2
    G.add_node("MH 3",    pos=(549, 645),  coords = (42.29261011959146, -71.26390792634388), pathway=False)  # MH 3
    G.add_node("WH 1",    pos=(830, 482),  coords = (42.293019830361196, -71.26295440109273), pathway=False)  # WH 1 (in)
    G.add_node("WH 2",    pos=(768, 427),  coords = (42.29318649160559, -71.26315556675328), pathway=False)  # WH 2 w
    G.add_node("WH 3",    pos=(911, 539),  coords = (42.29290277041453, -71.2627009323597), pathway=False)  # WH 3 e
    G.add_node("WH 4",    pos=(846, 432),  coords = (42.29314978649178, -71.26289941581034), pathway=False)  # WH 4 w lounge
    G.add_node("WH 5",    pos=(876, 474),  coords = (42.29305157539783, -71.26279078634431), pathway=False)  # WH 5 e lounge
    G.add_node("WH 6",    pos=(909, 323),  coords = (42.29341267402442, -71.26270361455002), pathway=False)  # WH 6 n
    G.add_node("EH 1",    pos=(1030, 649), coords = (42.29261111163257, -71.26224763901361), pathway=False)  # EH 1 (in)
    G.add_node("EH 2",    pos=(976, 576),  coords = (42.29278875392011, -71.26247385140057), pathway=False)  # EH 2 w
    G.add_node("EH 3",    pos=(1138, 703), coords = (42.29239031457536, -71.26195038758173), pathway=False)  # EH 3 e
    G.add_node("EH 4",    pos=(1063, 594), coords = (42.292724584494934, -71.26214138449437), pathway=False)  # EH 4 (in) w lounge
    G.add_node("EH 5",    pos=(1093, 619), coords = (42.292646745688444, -71.26204581431963), pathway=False)  # EH 5 e lounge
    G.add_node("EH 6",    pos=(1086, 482), coords = (42.293027263579965, -71.26207940607478), pathway=False)  # EH 6 n   # CHECK
    G.add_node("LPB",     pos=(248, 179),  coords = (42.293764694557765, -71.26489403407126), pathway=False)  # LPB
    G.add_node("Park 1",  pos=(196, 508),  coords = (42.29295691903568, -71.26511968235003), pathway=False)  # parking lot A
    G.add_node("TC",      pos=(366, 602),  coords = (42.29263151086271, -71.26455375403833), pathway=False)  # traffic circle
    G.add_node("Park 2",  pos=(1198, 612), coords = (42.29266880578926, -71.26171318420484), pathway=False)  # parking lot B

    with open(csv_path_nodes, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            if len(row) > 3:
                G.add_node(row[0], coords=(float(row[1]), float(row[2])), pos=(int(row[3]), int(row[4])), pathway="True")

    with open(csv_loc, mode='r') as csv_file:
        edge_counter = set()
        csv_reader = csv.reader(csv_file)
        first_row = True
        for row in list(csv_reader):
            if first_row:
                first_row = False
                continue
            #print(row)
            cur_node = row[0]
            for con_node in row[1:]:
                con_node = con_node.strip()
                if con_node:
                    if G.has_node(cur_node) and G.has_node(con_node):
                        add_dist_edge(G, cur_node, con_node)
                        if directed:
                            edge_tuple = (cur_node, con_node)
                        else:
                            edge_tuple = tuple(sorted([cur_node, con_node]))
                        edge_counter.add(edge_tuple)
                    else:
                        # The nodes in the CSV AREN'T in THE graph!!
                        if G.has_node(cur_node):
                            print(f"{con_node} is not in the networkx graph!")
                        else:
                            print(f"{cur_node} is not in the networkx graph!")

        # print(f'Added {len(edge_counter)} Unique edges to the graph from {csv_loc}')
        return G

def visualize_graph(G, node_list, start_node, end_node, save_fig=False, 
                    fig_name=None, new_edges=None, color="red"):
    """
    Displays the graph of nodes in node_list using Networkx and Matplotlib. If 
    save_fig=True, it does not display the graph but instead saves the entire 
    figure as a png.
    """
    all_olin_nodes = list(G.nodes())
    node_sizes = []
    node_labels = {}
    # pixel coordinates of node on satellite image of Olin's campus
    pos = nx.get_node_attributes(G, 'pos')
    pathway = nx.get_node_attributes(G, 'pathway')
    for i in all_olin_nodes:
        if i != start_node and i != end_node:
            if i in node_list:
                # hide pathway nodes from display
                if pathway[i]:
                    node_sizes.append(100)
                    node_labels[str(i)] = ""
                else:
                    # change to .append(x > 0) to display non-pathway nodes
                    node_sizes.append(100)
                    # change "" to str(i) to display node names
                    node_labels[str(i)] = "" #str(i)
            else:
                # remove unvisited nodes from display
                G.remove_node(i)
        else:
            # display start and end nodes and labels
            node_sizes.append(400)
            node_labels[str(i)] = str(i)

    plt.figure(figsize=(10, 8))
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw_networkx(G, pos, labels=node_labels, node_size=node_sizes, node_color=color, font_size=9)
    # display edge lengths in feet
    # labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edges(G, pos, width=3, edge_color=color)
    # display satellite image of Olin's campus as background
    data = mpimg.imread('./images/olin_sat.png')
    plt.imshow(data)
    # save the figure to path given by fig_name parameter if save_fig=True
    if save_fig:
        plt.savefig(fig_name)
    # display figure in pop-up
    else:
        plt.show()

def all_nodes(G):
    """
    Displays the graph of nodes in node_list using Networkx and Matplotlib. If 
    save_fig=True, it does not display the graph but instead saves the entire 
    figure as a png.
    """
    all_olin_nodes = list(G.nodes())
    node_sizes = []
    node_labels = {}
    # pixel coordinates of node on satellite image of Olin's campus
    pos = nx.get_node_attributes(G, 'pos')
    pathway = nx.get_node_attributes(G, 'pathway')
    for i in all_olin_nodes:
        # hide pathway nodes from display
        if pathway[i]:
            node_sizes.append(0)
            node_labels[str(i)] = ""
        else:
            # change to .append(x > 0) to display non-pathway nodes
            node_sizes.append(400)
            # change "" to str(i) to display node names
            node_labels[str(i)] = str(i)

    plt.figure(figsize=(10, 8))
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw_networkx(G, pos, labels=node_labels, node_size=node_sizes, node_color='red', font_size=9)
    # display edge lengths in feet
    # labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edges(G, pos, width=0)
    # display satellite image of Olin's campus as background
    data = mpimg.imread('./images/olin_sat.png')
    plt.imshow(data)
    plt.show()


def ordered_route(G, ordered_route):
    total_path = [ordered_route[0]]
    total_run_data = []
    for i in range(0,len(ordered_route)-1):
        print(f"Travelling from {ordered_route[i]} to {ordered_route[i+1]} ")
        astar_res = astar(G, ordered_route[i], ordered_route[i+1])
        if not astar_res:
            return "These nodes cannot be connected!" 
        total_path.extend(astar_res[0][1:])
        total_run_data.append(astar_res[1])
    return (total_path, total_run_data)

if __name__ == "__main__":
    # ret = astar(graph, "1", "3")
    # print(ret[0])
    # print(ret[1])

    g = build_graph(vis=False, directed=False)

    Start = "AC 1"
    End = "WH 1"
    A = astar(g, Start, End)
    visualize_graph(g, A[0], Start, End)

    # A = all_nodes(g)

