# modules/permission_analyzer.py

from config import DANGEROUS_PERMISSIONS

def find_dangerous_edges(G):

    dangerous = []

    for u, v, data in G.edges(data=True):

        perm = data.get("permission")

        if perm in DANGEROUS_PERMISSIONS:

            dangerous.append({
                "source": u,
                "target": v,
                "permission": perm
            })

    return dangerous
