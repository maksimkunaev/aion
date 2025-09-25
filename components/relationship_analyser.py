from constants.relationships import ALLOWED_RELATIONS


def analyze_relationships(graph, allowed_relations=None):
    if allowed_relations is None:
        allowed_relations = ALLOWED_RELATIONS

    edges = []
    nodes = graph["nodes"]
    seen = set()

    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i == j:
                continue

            a, b = nodes[i], nodes[j]

            if "is_in" in allowed_relations:
                if a["x"] == b["x"]:
                    # ограничение: связываем только "не-локация" → "локация/контейнер"
                    if a["type"] != "location":
                        key = (a["id"], b["id"])
                        if key not in seen:
                            edges.append(
                                {
                                    "relation": "is_in",
                                    "source": a["id"],
                                    "target": b["id"],
                                }
                            )
                            seen.add(key)

    return {"nodes": nodes, "edges": edges}
