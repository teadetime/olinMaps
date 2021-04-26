import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import PIL

def build_graph(vis=False):
    G = nx.Graph()
    G.add_node(1, pos = (313, 392))     # AC 1
    G.add_node(2, pos = (429, 226))     # AC 2
    G.add_node(3, pos = (596, 159))     # AC 3
    G.add_node(4, pos = (404, 160))     # AC 4
    G.add_node(5, pos = (629, 390))     # CC 1
    G.add_node(6, pos = (692, 392))     # CC 2 (lower)
    G.add_node(7, pos = (746, 291))     # CC 3 (lower)
    G.add_node(8, pos = (636, 154))     # CC 4
    G.add_node(9, pos = (503, 489))     # MH 1
    G.add_node(10, pos = (582, 552))    # MH 2
    G.add_node(11, pos = (572, 637))    # MH 3
    G.add_node(12, pos = (810, 503))    # WH 1 (in)
    G.add_node(13, pos = (760, 419))    # WH 2 w
    G.add_node(14, pos = (915, 530))    # WH 3 e
    G.add_node(15, pos = (853, 415))    # WH 4 w lounge
    G.add_node(16, pos = (882, 468))    # WH 5 e lounge
    G.add_node(17, pos = (909, 325))    # WH 6 n
    G.add_node(18, pos = (1030, 649))   # EH 1 (in)
    G.add_node(19, pos = (966, 565))    # EH 2 w
    G.add_node(20, pos = (1138, 703))   # EH 3 e
    G.add_node(21, pos = (1063, 594))   # EH 4 (in) w lounge
    G.add_node(22, pos = (1093, 619))   # EH 5 e lounge
    G.add_node(23, pos = (1121, 450))   # EH 6 n
    G.add_node(24, pos = (248, 179))    # LPB
    G.add_node(25, pos = (172, 562))    # parking lot
    G.add_node(26, pos = (366, 602))    # traffic circle
    G.add_node(27, pos = (1198, 612))   # LPB

    
    # G.add_edge(1,2, weight=2)
    # G.add_edge(2,3, weight=1)
    # G.add_edge(3,4, weight=5)
    # G.add_edge(1,4, weight=2)

    if vis:
        node_sizes = []
        for i in range(27):
            node_sizes.append(100)
        plt.figure(figsize=(7, 7))
        pos= nx.get_node_attributes(G, 'pos')
        nx.draw_networkx(G, pos, node_size = node_sizes)
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        data = mpimg.imread('./images/olin_sat.png')
        plt.imshow(data)
        plt.show()
    return G

def astar(G, start_node, end_node):
    pass


if __name__ == "__main__":
    # imgplot = plt.imshow(img)
    # plt.show()
    graph = build_graph(True)
    # astar(G, 1, 3)