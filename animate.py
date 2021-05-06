from astar import astar, build_graph, visualize_graph
import matplotlib.pyplot as plt
import imageio
from os import remove


def call_vis(k, start_node, end_node, c, draw_color):
    G=build_graph()
    visualize_graph(G, k, start_node, end_node, save_fig=True, fig_name=c, color=draw_color)

def get_figs(start_node, end_node):
    images = []
    img="./images/ani/img.png"
    g = build_graph()
    A = astar(g, start_node, end_node)
    explored = A[1]

    for i in explored:
        call_vis(i[0], start_node, end_node, img, 'orange')
        images.append(imageio.imread(img))
        remove(img)

    for i in range(2):
        call_vis(A[0], start_node, end_node, img, 'red')
        images.append(imageio.imread(img))
        remove(img)

    imageio.mimsave('./images/animation.gif', images, duration=.6)


get_figs("WH 1", "EH 1")