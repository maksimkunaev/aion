def get_world_model(graph):
    coords = {}
    step = 10

    # базовое размещение
    for i, node in enumerate(graph["nodes"]):
        coords[node["id"]] = i * step

    changed = True
    while changed:  # итеративно обновляем, пока что-то меняется
        changed = False
        for edge in graph["edges"]:
            rel = edge["relation"]
            if rel == "is_in":
                source, target = edge["source"], edge["target"]
                if target in coords and coords[source] != coords[target]:
                    coords[source] = coords[target]
                    changed = True

    # обновляем узлы
    for node in graph["nodes"]:
        node["x"] = coords[node["id"]]

    return graph
