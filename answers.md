# CMPS 2200 Recitation 10## Answers

**Name:**Justin Green


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
The reachable function serves as a graph traversal function which has a run time dependent on the number of edges and nodes. Initializing result and frontier requires work of O(1). The while loop runs once per reachable node from start_node. Each node is popped from frontier once, which contributes O(1) work. Then, each edge is examined, which contributes O(1) average work per node. Each process per node and edge contributes O(1) work, so the number of edges and nodes determines the amount of work. Therefore, the total work on average will be O(n + e) where n = the number of nodes and e = the number of edges.
- **4)**
The worst case is going to one call to reachable because the graph is either connected or not connected.
- **5)**
We would have the same work as the reachable function, O(n + e) where n = the number of nodes and e = the number of edges. This is because each step of the function requires O(1) besides calling reachable, which requires O(n + e) work. First, we check if we have a graph or not, then we get one arbitrary node, we call reachable, and finally, we check to see if the number of reachable nodes is the same as the number of nodes in the graph to ensure if the graph is connected.
- **7)**
Switching to an adjacency matrix would require us to process each node in an entire row of length n nodes. The work done per node is O(n) where n = the number of nodes just as before, but now we are doing that each individual node to determine its neighbors. This means O(n) work per node times n nodes = O(n^2). So, our work will now be O(n^2) instead of O(n + m) because of our repeated scanning