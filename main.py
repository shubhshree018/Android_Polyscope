# main.py

from modules.parser import parse_mac_policy
from modules.graph_builder import build_policy_graph
from modules.permission_analyzer import find_dangerous_edges
from modules.path_finder import find_privilege_paths
from modules.report import print_report


def main():

    file_path = "output/mac_expanded.txt"

    print("Parsing SELinux policy...")
    rules = parse_mac_policy(file_path)

    print("Building policy graph...")
    graph = build_policy_graph(rules)

    print("Analyzing dangerous permissions...")
    dangerous = find_dangerous_edges(graph)

    print("Searching privilege escalation paths...")
    paths = find_privilege_paths(graph)

    print_report(graph, dangerous, paths)


if __name__ == "__main__":
    main()
