from astar import astar, build_graph, visualize_graph
import matplotlib.pyplot as plt
import imageio
from os import remove


def call_vis(k, start_node, end_node, c, draw_color):
    G=build_graph()
    visualize_graph(G, k, start_node, end_node, save_fig=True, fig_name=c, color=draw_color)

def get_figs(start_node, end_node):
    images = []
    # where to save image
    img="./images/ani/img.png"
    g = build_graph()
    A = astar(g, start_node, end_node)
    # use the "process" part of the astar output
    explored = A[1]

    for i in explored:
        # call the stupid function I made at some point just calling 
        # visualize_graph, I forget why will correct later
        call_vis(i[0], start_node, end_node, img, 'orange')
        # append the image to list of images to use in animation
        images.append(imageio.imread(img))
        # clean the image dir
        remove(img)

    # display final solution for twice as long as normal frame
    for i in range(2):
        call_vis(A[0], start_node, end_node, img, 'red')
        images.append(imageio.imread(img))
        remove(img)

    # compile the animation from images list
    imageio.mimsave(f"./images/{start_node}_{end_node}.gif", images, duration=.6)


get_figs("AC 1", "EH 1")