<!-- this report should detail background research, explain the final algorithm, and detail and interpret the results (similar to QMRI format)

Graded on:
1. Motivation: Start with an interesting and appropriate application area, question, or problem and provide motivation behind studying it.

2. Design: For theory-based, conduct a thorough and relevant literature review. For implementation-based, detail how the design process including any assumptions that are made and how relevant literature informs the process.

3. Analysis: For theory-based, provide a synthesis of the results of your literature review that highlights the overall landscape. For implementation-based, validate your program

4. Report: Present and communicate about your decisions and results in a clear and precise manner.


 -->

## Introduction
This project seeks to implement a quickest-route finder at a small scale: using the Olin college campus. In olinMaps, we sought to explore how we can implement path planning between multiple points, in the way that sites such as Google Maps are able to do.

Once a map reaches a certain size, it is not viable to test all possible routes from a start point to an end point, and so we start to look for algorithms to reduce the search space. The field of path planning is well studied, with several algorithms (namely Dijkstras and A*) that are directly applicable and well documented that we can apply towards our problem.



<!-- Path planning is also connected to more complex problems like route-optimization.

This gives us easy access to data as we are able to validate the paths we generate by walking them ourselves. -->


## Project Design
This project is composed of three different parts:
1. Creating a graph representation of Olin
2. Creating an A* implementation that can use our graph
3. Visualize the algorithm and the process


#### Olin Graph Creation

To create the graph, we first figured out relevant locations at Olin to be valid locations for navigation to and from. These points are the principal nodes of our graph. We decided to also find intermediary nodes (such as sidewalk intersections) that would make it easy to connect these principal nodes, mapping our graph closely to the physical layout of Olin's campus.

We took advantage of Google Maps satellite and location data to find longitude and latitude positions for our elements on the map, and use these to calculate the distance/weight between the nodes by using a [haversine function](https://pypi.org/project/haversine/). Using this distance calculation assumes a flat map (does not account for elevation change in things like stairways. elevators etc), but it is a good estimation for the majority of these paths.


We use the [networkx python package](https://networkx.org/) data structures to store the graph.


#### A* Algorithm
The [A* algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm) intelligently explores the search space by modifying [Djikstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) with the use of a heuristic. This heuristic guides the algorithm’s exploration towards the optimal solution more quickly. A* implementations for spatial mapping commonly use a heuristic that is the shortest distance to the end target. A more complicated heuristic is needed when navigating a more complex map (ie. a map that considers elevators, stairs). Our implemented heuristic is the distance between the nodes using the haversine function.

<!-- We hope to expand this project into a more complicated map environment such that it could find optimal routes with things like stairwells and numbers of doors accounted for. -->

Our implementation of A* is based on the teaching materials for Olin's Data Structures and Algorithms course and an associated homework. [**ISNERT LINKS HERE**]


#### Visualize the Algorithm
Creating good visualizations for our path planning algorithm was also critical to demonstrating our results.
<!-- Maybe also demonstrating how the algorithm works. -->

Since our map is structured using with latitude and longitude coordinates, which at our scale simplifies essentially to 2D, we decided to map our coordinates onto an aerial shot of the Olin Campus from Google Maps. This way we can easily show a viewer what the result of our algorithm looks like, and it also allows for us to visualize how the A* algorithm searched for this path.




## Analysis
Below is a test case for our final implementation as a walk-through.

<!-- See link to jupyter notebook or whatever if we get it running here -->

**INSERT GIUF HERE![]()**

This shows the best path from points A TO B along with a distance of ____. This is the shortest way between these two nodes.
<!-- A more complex path such as ____ is shown below
INSET HERE -->

Our algorithm reaches it’s limitation when presented with a route optimization problem that lists destinations without an associated order. However, if the order of destinations is known our algorithm can successfully find an optimal path. INESRT EXAMPLE OF MULTI STOP ROUTE in which the order is known.

To illustrate how this algorithm is limited by the ordering of the stops, here is the same path with a different input order.

<!-- Need a section on validation -->



## Future Goals/Direction of work

Some possible future elaborations on this work are listed below:

- Explore other methods of map storage (perhaps storing obstacles would be better for a sparse environment)
- 3d building path planning (For very large buildings, what is the quickest way to get from point a to b). This could have safety implications.
- Compare different methods of doing route optimization/ordering of stops. For small problems, it is feasible to check all possibilities but this changes once there is a large map and many stops.
- What other data should be stored as operations are carried out in order to speed up other route findings. Does storing paths for main nodes or frequently
-Future optimization in which we could interface with google’s api’s to build our own version of maps for a given space.
