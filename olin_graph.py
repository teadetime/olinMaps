import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import PIL
from matplotlib.animation import FuncAnimation, PillowWriter  
from haversine import haversine, Unit


def build_graph(vis=False):
    G = nx.Graph()
    G.add_node("AC 1",    pos=(324, 403),  coords = (42.29321996991126, -71.26459288853798))  #  AC 1
    G.add_node("AC 2",    pos=(456, 240),  coords = (42.29363418081095, -71.26422001841294))  # AC 2
    G.add_node("AC 3",    pos=(599, 149),  coords = (42.29386690104804, -71.2637380411814))   # AC 3
    G.add_node("AC 4",    pos=(404, 160),  coords = (42.29382686013987, -71.26440227411027))  # AC 4
    G.add_node("CC 1",    pos=(653, 376),  coords = (42.29328713953713, -71.26356098757215))  # CC 1
    G.add_node("CC 2",    pos=(717, 396),  coords = (42.29322457502598, -71.26333431385294))  # CC 2 (lower)
    G.add_node("CC 3",    pos=(758, 266),  coords = (42.29354657304486, -71.26318545348332))  # CC 3 (lower)
    G.add_node("CC 4",    pos=(636, 154),  coords = (42.29384938315572, -71.2636004581119))  # CC 4
    G.add_node("MH 1",    pos=(499, 488),  coords = (42.2930076842383, -71.26406733829359))  # MH 1
    G.add_node("MH 2",    pos=(582, 536),  coords = (42.29290340955621, -71.26378991671152))  # MH 2
    G.add_node("MH 3",    pos=(549, 645),  coords = (42.29261011959146, -71.26390792634388))  # MH 3
    G.add_node("WH 1",    pos=(830, 482),  coords = (42.293019830361196, -71.26295440109273))  # WH 1 (in)
    G.add_node("WH 2",    pos=(768, 427),  coords = (42.29318649160559, -71.26315556675328))  # WH 2 w
    G.add_node("WH 3",    pos=(911, 539),  coords = (42.29290277041453, -71.2627009323597))  # WH 3 e
    G.add_node("WH 4",    pos=(846, 432),  coords = (42.29314978649178, -71.26289941581034))  # WH 4 w lounge
    G.add_node("WH 5",    pos=(876, 474),  coords = (42.29305157539783, -71.26279078634431))  # WH 5 e lounge
    G.add_node("WH 6",    pos=(909, 323),  coords = (42.29341267402442, -71.26270361455002))  # WH 6 n
    G.add_node("EH 1",    pos=(1030, 649), coords = (42.29261111163257, -71.26224763901361))  # EH 1 (in)
    G.add_node("EH 2",    pos=(976, 576),  coords = (42.29278875392011, -71.26247385140057))  # EH 2 w
    G.add_node("EH 3",    pos=(1138, 703), coords = (42.29239031457536, -71.26195038758173))  # EH 3 e
    G.add_node("EH 4",    pos=(1063, 594), coords = (42.292724584494934, -71.26214138449437))  # EH 4 (in) w lounge
    G.add_node("EH 5",    pos=(1093, 619), coords = (42.292646745688444, -71.26204581431963))  # EH 5 e lounge
    G.add_node("EH 6",    pos=(1086, 482), coords = (42.293027263579965, -71.26207940607478))  # EH 6 n   # CHECK
    G.add_node("LPB",     pos=(248, 179),  coords = (42.293764694557765, -71.26489403407126))  # LPB
    G.add_node("Park 1",  pos=(196, 508),  coords = (42.29295691903568, -71.26511968235003))  # parking lot A
    G.add_node("TC",      pos=(366, 602),  coords = (42.29263151086271, -71.26455375403833))  # traffic circle
    G.add_node("Park 2",  pos=(1198, 612), coords = (42.29266880578926, -71.26171318420484))  # parking lot B

    # G.add_edge(1,2, weight=2)
    # G.add_edge(2,3, weight=1)
    # G.add_edge(3,4, weight=5)
    # G.add_edge(1,4, weight=2)

    if vis:
        node_sizes = []
        for i in range(27):
            node_sizes.append(100)
        plt.figure(figsize=(9, 9))
        pos = nx.get_node_attributes(G, 'pos')
        nx.draw_networkx(G, pos, node_size=node_sizes)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        data = mpimg.imread('./images/olin_sat.png')
        plt.imshow(data)
        plt.show()
    return G


def add_dist_edge(graph, node1, node2, unit = "ft"):
    """
    Creates edges for nodes on the graph based on the distance between lat and long (haversine function)

    :param graph: networkx graph
    :param node1: Name of node
    :param node2:
    :param unit: unit for haversine calc
    """

    coords1 = graph.nodes[node1].coords
    coords2 = graph.nodes[node2].coords

    graph.add_edge(node1, node2, weight = haversine(coords1,coords2, unit=unit))


if __name__ == "__main__":
    graph = build_graph(True)

    AC1 = (42.29321996991126, -71.26459288853798)  #  AC 1
    AC2 = (42.29363418081095, -71.26422001841294)  # AC 2

    dist = haversine(AC1, AC2, unit='ft')

    print(dist)
