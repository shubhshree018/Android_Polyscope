# modules/path_finder.py

import networkx as nx
from config import START_DOMAINS, TARGET_DOMAINS

def find_privilege_paths(G):

    paths = []

    for start in START_DOMAINS:

        if start not in G:
            continue

        for target in TARGET_DOMAINS:

            if target not in G:
                continue

            try:
                found = nx.all_simple_paths(
                    G,
                    source=start,
                    target=target,
                    cutoff=5
                )

                for p in found:
                    paths.append(p)

            except:
                continue

    return paths
