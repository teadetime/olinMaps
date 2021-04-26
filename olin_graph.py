import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import PIL


def build_graph(vis=False):
    G = nx.Graph()
    G.add_node("AC 1",    pos=(313, 392),  coords = (42.29321996991126, -71.26459288853798))  #  AC 1
    G.add_node(2,         pos=(429, 226),  coords = (42.29363418081095, -71.26422001841294))  # AC 2
    G.add_node(3,         pos=(596, 159),  coords = (42.29386690104804, -71.2637380411814))  # AC 3
    G.add_node(4,         pos=(404, 160),  coords = (42.29382686013987, -71.26440227411027))  # AC 4
    G.add_node(5,         pos=(629, 390),  coords = (42.29328713953713, -71.26356098757215))  # CC 1
    G.add_node(6,         pos=(692, 392),  coords = (42.29322457502598, -71.26333431385294))  # CC 2 (lower)
    G.add_node(7,         pos=(746, 291),  coords = (42.29354657304486, -71.26318545348332))  # CC 3 (lower)
    G.add_node(8,         pos=(636, 154),  coords = (42.29384938315572, -71.2636004581119))  # CC 4
    G.add_node(9,         pos=(503, 489),  coords = (42.2930076842383, -71.26406733829359))  # MH 1
    G.add_node(10,        pos=(582, 552),  coords = (42.29290340955621, -71.26378991671152))  # MH 2
    G.add_node(11,        pos=(572, 637),  coords = (42.29261011959146, -71.26390792634388))  # MH 3
    G.add_node(12,        pos=(810, 503),  coords = (42.293019830361196, -71.26295440109273))  # WH 1 (in)
    G.add_node(13,        pos=(760, 419),  coords = (42.29318649160559, -71.26315556675328))  # WH 2 w
    G.add_node(14,        pos=(915, 530),  coords = (42.29290277041453, -71.2627009323597))  # WH 3 e
    G.add_node(15,        pos=(853, 415),  coords = (42.29314978649178, -71.26289941581034))  # WH 4 w lounge
    G.add_node(16,        pos=(882, 468),  coords = (42.29305157539783, -71.26279078634431))  # WH 5 e lounge
    G.add_node(17,        pos=(909, 325),  coords = (42.29341267402442, -71.26270361455002))  # WH 6 n
    G.add_node(18,        pos=(1030, 649), coords = (42.29261111163257, -71.26224763901361))  # EH 1 (in)
    G.add_node(19,        pos=(966, 565),  coords = (42.29278875392011, -71.26247385140057))  # EH 2 w
    G.add_node(20,        pos=(1138, 703), coords = (42.29239031457536, -71.26195038758173))  # EH 3 e
    G.add_node(21,        pos=(1063, 594), coords = (42.292724584494934, -71.26214138449437))  # EH 4 (in) w lounge
    G.add_node(22,        pos=(1093, 619), coords = (42.292646745688444, -71.26204581431963))  # EH 5 e lounge
    G.add_node(23,        pos=(1121, 450), coords = (42.293027263579965, -71.26207940607478))  # EH 6 n   # CHECK
    G.add_node(24,        pos=(248, 179),  coords = (42.293764694557765, -71.26489403407126))  # LPB
    G.add_node(25,        pos=(172, 562),  coords = (42.29295691903568, -71.26511968235003))  # parking lot A
    G.add_node(26,        pos=(366, 602),  coords = (42.29263151086271, -71.26455375403833))  # traffic circle
    G.add_node(27,        pos=(1198, 612), coords = (42.29266880578926, -71.26171318420484))  # parking lot B

    # G.add_edge(1,2, weight=2)
    # G.add_edge(2,3, weight=1)
    # G.add_edge(3,4, weight=5)
    # G.add_edge(1,4, weight=2)

    if vis:
        node_sizes = []
        for i in range(27):
            node_sizes.append(100)
        plt.figure(figsize=(7, 7))
        pos = nx.get_node_attributes(G, 'pos')
        nx.draw_networkx(G, pos, node_size=node_sizes)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        data = mpimg.imread('./images/olin_sat.png')
        plt.imshow(data)
        plt.show()
    return G



if __name__ == "__main__":
    # imgplot = plt.imshow(img)
    # plt.show()
    graph = build_graph(True)
    # astar(G, 1, 3)