from map import GraphMapCreator
from metrics import euclidean
from graph_generator import GraphGenerator
from graph_visualizer import GraphVisualizer
from ant_colony_optimizer import AntColonyOptimizer
from example_data import nodes_data, neighbors_data
# Example usage:
graph_generator = GraphGenerator()
nodes_set, edges_set = graph_generator.generate_graph()
# Visualization of random generated graph
graph_visualizer = GraphVisualizer(nodes_set, edges_set)
graph_visualizer.visualize_graph()
# Optimizing random graph using ACO
random_graph_map = GraphMapCreator(nodes_set, edges_set, 'Q1', 'O1')
aco_optimizer = AntColonyOptimizer(random_graph_map, euclidean)
optimized_nodes, optimized_neighbors = aco_optimizer.solve_aco()
# Visualization of optimal path for random graph
graph_visualizer = GraphVisualizer(optimized_nodes, optimized_neighbors)
graph_visualizer.visualize_graph()
# Visualization of provided data
graph_visualizer = GraphVisualizer(nodes_data, neighbors_data, 10, 10, 70)
graph_visualizer.visualize_graph()
# Creating graph_map object and optimizing it via ACO
graph_map = GraphMapCreator(nodes_data, neighbors_data, 'A', 'G')
aco_optimizer = AntColonyOptimizer(graph_map, euclidean)
optimized_nodes, optimized_neighbors = aco_optimizer.solve_aco()
# Visualization of optimal path
graph_visualizer = GraphVisualizer(optimized_nodes, optimized_neighbors, 10, 10, 70)
graph_visualizer.visualize_graph()
