# modules/report.py

def print_report(graph, dangerous_edges, paths):

    print("\n====== PolyScope Analysis Report ======\n")

    print("Total Nodes:", len(graph.nodes()))
    print("Total Edges:", len(graph.edges()))

    print("\nDangerous Permissions Found:", len(dangerous_edges))

    for edge in dangerous_edges[:10]:

        print(
            edge["source"],
            "→",
            edge["target"],
            "(",
            edge["permission"],
            ")"
        )

    print("\nPrivilege Escalation Paths:", len(paths))

    for p in paths[:10]:
        print(" → ".join(p))
