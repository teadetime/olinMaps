from astar import astar, build_graph, visualize_graph
import matplotlib.pyplot as plt
import imageio
from os import remove


def animation(start_node, end_node):
    images = []
    # where to save image
    img="./images/ani/img.png"
    g = build_graph()
    A = astar(g, start_node, end_node)
    # use the "process" part of the astar output
    explored = A[1]

    for i in explored:
        # plot the graph at each step in astar
        G=build_graph()
        visualize_graph(G, i[0], start_node, end_node, save_fig=True, fig_name=img, color='orange')
        # append the image to list of images to use in animation
        images.append(imageio.imread(img))
        # clean the image dir
        remove(img)

    # display final solution for twice as long as normal frame
    for i in range(2):
        visualize_graph(G, A[0], start_node, end_node, save_fig=True, fig_name=img, color='red')
        images.append(imageio.imread(img))
        remove(img)

    # compile the animation from images list
    imageio.mimsave(f"./images/{start_node}_{end_node}.gif", images, duration=.6)

if __name__ == "__main__":
    Start = "AC 1"
    End = "EH 1"
    animation(Start, End)