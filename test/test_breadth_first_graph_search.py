from peas.map import create_map
from peas.map_search_problem import MapSearchProblem
from searchs.breadth_first_graph_search import breadth_first_graph_search


def test_breadth_first_graph_search():
    pitts_map = create_map()
    pitts_problem = MapSearchProblem('656071251', '105012740', pitts_map)
    goal_node, explored_nodes, frontier_length_nodes = breadth_first_graph_search(pitts_problem)

    rute = goal_node.solution()

    print("Número de nodos visitados: {}".format(len(explored_nodes)))
    print("Número de nodos en memoria: {}".format(len(explored_nodes) + frontier_length_nodes))
    print("Número de nodos en la ruta encontrada: {}".format(len(rute)))
    print("Costo de la ruta encontrada: {} Km".format(goal_node.path_cost))
