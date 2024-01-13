import random

class GraphGenerator:
    def __init__(self, num_of_nodes=30, num_of_edges_min=1, num_of_edges_max=4):
        self.num_of_nodes = num_of_nodes
        self.num_of_edges_min = num_of_edges_min
        self.num_of_edges_max = num_of_edges_max

    def generate_graph(self):
        value_of_x_max, value_of_y_max = 50, 50

        set_of_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        nodes_set = {}
        edges_set = {}

        if self.num_of_nodes <= len(set_of_letters):
            for i in range(self.num_of_nodes):
                nodes_set[set_of_letters[i]] = (random.randint(0, value_of_x_max), random.randint(0, value_of_y_max))
        else:
            for k in range(len(set_of_letters)):
                if len(nodes_set) < self.num_of_nodes:
                    for j in range(len(set_of_letters)):
                        nodes_set[set_of_letters[j] + str(k+1)] = (random.randint(0, value_of_x_max), random.randint(0, value_of_y_max))
                        if len(nodes_set) == self.num_of_nodes:
                            break

        edges_names = list(nodes_set)
        for edge_name in edges_names:
            edges_set[edge_name] = []

        for edge_name in edges_names:
            edge_value = edges_set[edge_name]
            num_of_edges = random.randint(self.num_of_edges_min, self.num_of_edges_max - 1)

            while len(edge_value) < num_of_edges:
                random_node_index = random.randint(0, self.num_of_nodes - 1)
                random_node_name = edges_names[random_node_index]

                if random_node_name in edge_value or random_node_name == edge_name:
                    continue
                else:
                    if len(edge_value) >= self.num_of_edges_max:
                        continue
                    elif random_node_name in edges_set and len(edges_set[random_node_name]) >= self.num_of_edges_max:
                        continue
                    else:
                        edge_value.append(edges_names[random_node_index])

                        if random_node_name in edges_set:
                            if edge_name in edges_set[random_node_name]:
                                continue
                            else:
                                edges_set[random_node_name].append(edge_name)
                        else:
                            edges_set[random_node_name] = [edge_name]

        # Convert edge values from list to tuple
        for edge_name in edges_names:
            edges_set[edge_name] = tuple(edges_set[edge_name])

        return nodes_set, edges_set