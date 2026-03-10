# modules/parser.py

def parse_mac_policy(file_path):
    rules = []

    with open(file_path) as f:
        for line in f:
            parts = line.strip().split()

            if len(parts) != 4:
                continue

            src, tgt, obj_class, perm = parts

            rule = {
                "source": src,
                "target": tgt,
                "class": obj_class,
                "permission": perm
            }

            rules.append(rule)

    return rules
