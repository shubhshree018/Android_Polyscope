# modules/graph_builder.py

import networkx as nx

def build_policy_graph(rules):

    G = nx.DiGraph()

    for rule in rules:

        src = rule["source"]
        tgt = rule["target"]

        G.add_edge(
            src,
            tgt,
            obj_class=rule["class"],
            permission=rule["permission"]
        )

    return G
