<!-- this report should detail background research, explain the final algorithm, and detail and interpret the results (similar to QMRI format) -->

## Introduction
This project seeks to explore how we can implement path planning between multiple points, in the way that sites such as Google Maps are able to do. This problem is interesting because it is not viable to test all permutations of a route once a map(graph) reaches a certain size. This problem is worth exploring as it leads to more complex and important problems like route-optimization. Path planning is also an approachable problem since there are several algorithms (namely Dijkstras and A*) that are directly applicable and well documented already.
This project seeks to implement a quickest-route finder for at a small scale: our college campus. This gives us easy access to data as we are able to validate the paths we generate by walking them ourselves.


## Design
This project can be broken down into three different parts
- Creating a graph representation of Olin
- Creating an A* implementation that can use our graph
- Visualize the algorithm and the process


#### Olin Graph Creation

To create the graph, we first figured out relevant locations at Olin to be valid locations for navigation to and from. These points are the principal nodes of our graph. We decided to also find intermediary nodes (such as sidewalk intersections) that would make it easy to connect these principal nodes, mapping our graph closely to the physical layout of Olin's campus.

We took advantage of Google Maps satellite and location data to find longitude and latitude positions for our elements on the map, and use these to calculate the distance/weight between the nodes by using a [haversine function](https://pypi.org/project/haversine/). Using this distance calculation assumes a flat map (does not account for elevation change in things like stairways. elevators etc), but it is a good estimation for the majority of these paths.


We decided to use the [networkx python package](https://networkx.org/) data structures to store the graph.


#### A* Algorithm
The [A* algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm) intelligently explores the search space by modifying [Djikstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) with the use of a heuristic. This heuristic guides the algorithm’s exploration towards the optimal solution more quickly. Most common A* implementations for spatial mapping use a heuristic that is the shortest distance to the end target. A more complicated heuristic is needed when navigating a more complex map (ie elevators stairs etc). Our implemented heuristic is the distance between the nodes using the haversine function.

We hope to expand this project into a more complicated map environment such that it could find optimal routes with things like stairwells and numbers of doors accounted for.
The page HERE FINSD SOURCE is loosely what our implementation is based on


#### Visualize the Algorithm
Creating good visualizations for our route-planning algorithm was also critical. Since our map is structured nicely with latitude and longitude coordinates and we are only dealing in 2d, we have decided to map our coordinates onto an aerial shot of the Olin Campus from Google Maps. This also lends itself to future optimization in which we could interface with google’s api’s to build our own version of maps for a given space.

We have developed our algorithm such that output shows how the final path was chosen so that someone not familiar with it can understand what was  happening.


## Analysis
Below is our final implementation. INSERT GIUF HERE![]()
This shows the best path from points A TO B along with a distance of ____. This is the shortest way between these two nodes.
A more complex path such as ____ is shown below
INSET HERE

Our algorithm reaches it’s limitation when presented with a route optimization problem that lists destinations without an associated order. However, if the order of destinations is known our algorithm can successfully find an optimal path. INESRT EXAMPLE OF MULTI STOP ROUTE in which the order is known.

To illustrate how this algorithm is limited by the ordering of the stops, here is the same path with a different input order.


## Future Goals/Direction of work
- Explorer other methods of map storage since maps are rarely made up of discrete points. (maybe storing obstacles would be better for a sparse environment)
- 3d building path planning (For very large buildings, what is the quickest way to get from point a to b). This could have safety implications.
- Compare different methods of doing route optimization/ordering of stops. For small problems, it is feasible to check all possibilities but this changes once there is a large map and many stops.
- What other data should be stored as operations are carried out in order to speed up other route findings. Does storing paths for main nodes or frequently
