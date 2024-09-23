# STEPS: 
# 1. Assign starting node
# 2. Assign distances to all other nodes to infinity
# 2. Assign all node with min distance as unknown
# 2. That distance is 0
# 3. Find the neighbor with the shortest this will be the current node.
# 4. Examine neighbors of current node.  If the neighbor's distance is greater than the distance we would get passing from the current node to this neighbor node, set that distance as the new min distance and the current node as the node to get there. 
# 5. Repeat until all nodes have been visited. 

graph = [
    [0, 1, 4, 0],
    [0, 0, 2, 5],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
big_num = 10000000000
starting_node = 0 

def get_best_option(distances, visited):
    min_len = big_num
    best_option_index = -1

    for i in range(len(distances)):
        if( distances[i] < min_len and visited[i] == False):
            min_len = distances[i]
            best_option_index = i 

    return best_option_index

def print_result(distances):
    for i in range(len(distances)):
        print(f"For Vertex {i} shortest is {distances[i]}")

def dijkstra(graph, starting_node):
    num_of_nodes = len(graph)
    distances = [big_num] * num_of_nodes
    visited = [False] * num_of_nodes 

    distances[starting_node] = 0

    for node in range(num_of_nodes):
        
        # find closet neighbor
        best_option_index = get_best_option(distances, visited)
        # Consider that node visited (we could do this later as well)
        visited[best_option_index] = True

        # from this new current node see if any distances are better 
        # than the distance currently assigned to it. 
        for i in range(num_of_nodes):
            if(visited[i] == False
               and graph[best_option_index][i] != 0
               and graph[best_option_index][i] != big_num
               and distances[i] > distances[best_option_index] + graph[best_option_index][i]
            ):
                distances[i] = distances[best_option_index] + graph[best_option_index][i]
    
    print_result(distances)

dijkstra(graph, starting_node)
