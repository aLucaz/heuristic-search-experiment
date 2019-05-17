from peas.node import Node


def depth_limited_search(problem, limit):
    return recursive_dls(Node(problem.initial), problem, limit)


def recursive_dls(node, problem, limit):
    """
    :param limit: int
    :param node: Node
    :type problem: MapSearchProblem
    """
    if problem.goal_test(node.state):
        return node.solution()

    elif limit == 0:
        return "cutoff"

    else:
        cutoff_flag = False
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            result = recursive_dls(child, problem, limit - 1)

            if result == "cutoff":
                cutoff_flag = True

            elif result is None:
                return result

        return "cutoff" if cutoff_flag else None
