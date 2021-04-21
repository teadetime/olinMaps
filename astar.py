import networkx as nx
import matplotlib.pyplot as plt

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
    pass


if __name__ == "__main__":
    graph = build_graph()
    #astar(G, 1, 3)