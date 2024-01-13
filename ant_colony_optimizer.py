from datetime import datetime
import numpy as np

class AntColonyOptimizer:
    def __init__(self, maps, metric, heuristic_coefficient=1, feromones_coefficient=1, ants_numb=5, repetitions_numb=10):
        self.maps = maps
        self.metric = metric
        self.heuristic_coefficient = heuristic_coefficient
        self.feromones_coefficient = feromones_coefficient
        self.ants_numb = ants_numb
        self.repetitions_numb = repetitions_numb

    def solve_aco(self):
        start_time = datetime.now()
        ants = self.ants_numb
        repetitions = self.repetitions_numb
        every_trial_in_graph = {}

        for i in self.maps.nodes:
            node1 = i
            if type(self.maps.neighbors[i]) == tuple:
                for j in self.maps.neighbors[i]:
                    node2 = j
                    single_trial = frozenset({node1, node2})
                    if single_trial not in every_trial_in_graph.keys():
                        every_trial_in_graph.update({single_trial: 1})
            else:
                single_trial = frozenset({node1, self.maps.neighbors[i]})

        for repetition in range(repetitions):
            list_of_tracks_of_every_ant = []
            last_repetition_roads = {}

            for ant in range(ants):
                current_node = self.maps.begin
                nodes_visited_by_ant = [self.maps.begin]

                while current_node != self.maps.end:
                    if type(self.maps.neighbors[current_node]) == tuple:
                        neighbour_nodes = list(self.maps.neighbors[current_node])
                    else:
                        neighbour_nodes = []
                        neighbour_nodes.append(self.maps.neighbors[current_node])

                    nodes_to_choose = []

                    for node in neighbour_nodes:
                        if node not in nodes_visited_by_ant:
                            nodes_to_choose.append(node)

                    if self.maps.end in nodes_to_choose:
                        choosen_node = self.maps.end
                    else:
                        if nodes_to_choose == []:
                            nodes_to_choose = neighbour_nodes

                        sum_for_probability = 0

                        for node in nodes_to_choose:
                            heuristic = self.metric(self.maps.nodes[node], self.maps.nodes[current_node]) / self.metric(self.maps.nodes[node], self.maps.nodes[self.maps.end])
                            feromones = every_trial_in_graph[frozenset({current_node, node})]
                            sum_for_probability += (heuristic**self.heuristic_coefficient) * (feromones**self.feromones_coefficient)

                        random_for_probability = np.random.random_sample()
                        chance_sum = 0

                        for node in nodes_to_choose:
                            heuristic = self.metric(self.maps.nodes[node], self.maps.nodes[current_node]) / self.metric(self.maps.nodes[node], self.maps.nodes[self.maps.end])
                            feromones = every_trial_in_graph[frozenset({current_node, node})]
                            chance_sum += (heuristic**self.heuristic_coefficient) * (feromones**self.feromones_coefficient) / sum_for_probability

                            if chance_sum > random_for_probability:
                                choosen_node = node
                                break

                    nodes_visited_by_ant.append(choosen_node)
                    current_node = choosen_node

                road_of_current_ant_using_trials = []

                for k in range(len(nodes_visited_by_ant) - 1):
                    road_of_current_ant_using_trials.append(frozenset({nodes_visited_by_ant[k], nodes_visited_by_ant[k+1]}))

                list_of_tracks_of_every_ant.append(road_of_current_ant_using_trials)

                if repetition == (repetitions - 1):
                    if tuple(nodes_visited_by_ant) in last_repetition_roads:
                        last_repetition_roads[tuple(nodes_visited_by_ant)] += 1
                    else:
                        last_repetition_roads[tuple(nodes_visited_by_ant)] = 1

            for trial in every_trial_in_graph:
                every_trial_in_graph[trial] = every_trial_in_graph[trial] * 0.5

            for track in list_of_tracks_of_every_ant:
                track_length = 0

                for trial_nodes in track:
                    trial_as_list = list(trial_nodes)
                    track_length += self.metric(self.maps.nodes[trial_as_list[0]], self.maps.nodes[trial_as_list[1]])

                for trial_nodes in track:
                    every_trial_in_graph[trial_nodes] += 5 / (track_length - self.metric(self.maps.nodes[self.maps.begin], self.maps.nodes[self.maps.end])) ** 3

        end_time = datetime.now()
        print(last_repetition_roads)
        
        def length_of_road(list1, points, metric):
            sums = 0
            for i in range(len(list1)-1):
                sums += metric(points[list1[i]], points[list1[i+1]])
            return sums

        for i in list(last_repetition_roads.keys()):
            print("Length of the path:", i)
            print(length_of_road(i, self.maps.nodes, self.metric))

        print("Execution Time:")
        print(end_time - start_time)
        optimized_path = list(last_repetition_roads.keys())[-1]
        optimized_nodes = {key: value for key, value in self.maps.nodes.items() if key in optimized_path}
        optimized_neighbors = {key: tuple(value for value in values if value in optimized_path) for key,values in self.maps.neighbors.items() if key in optimized_path}
        return optimized_nodes, optimized_neighbors