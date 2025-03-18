You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

 1. problem understanding 
The problem gives an undirected, connected graph represented as adjacency list.

2. thought 
We need to track both the current and which nodes have been visited.
Use a bitmask to represent the visited set: (1 << n) -1 represents the state.

3. search method 
apprently a BFS problem, so we use BFS 
define a state as (current node, visited_mask), when expanding, for each neighbor update mask
each state may expand to at most n neighbors.

4. Reference 
https://leetcode.com/problems/shortest-path-visiting-all-nodes/description/ Leetcode 847

5. Link of Video Recording:
