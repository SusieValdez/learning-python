from collections import defaultdict


def create_graph():
    graph = defaultdict(lambda: defaultdict(int))
    names = []
    with open("bible.txt") as f:
        bible_contents = f.read()[:1000000]
    print(len(bible_contents))
    with open("comp_sci.txt") as f:
        comp_sci_contents = "\n" + f.read()
    print(len(comp_sci_contents))

    contents = bible_contents + comp_sci_contents

    tokens = contents.split()
    num_tokens = len(tokens)
    token_set = list(set(tokens))
    num_states = len(token_set)

    token_to_state = {}
    for state, token in enumerate(token_set):
        print(f"initialising {state + 1} / {num_states}")
        token_to_state[token] = state
        names.append(token)

    connections_counts = defaultdict(lambda: defaultdict(int))
    for i, token in enumerate(tokens[:-1]):
        print(f"counting {i + 1} / {num_tokens}")
        next_token = tokens[i + 1]
        state = token_to_state[token]
        next_state = token_to_state[next_token]
        connections_counts[state][next_state] += 1

    print(connections_counts)

    for i, row in connections_counts.items():
        print(f"building graph {i + 1} / {num_states}")
        row_sum = sum(row.values())
        for j, col in row.items():
            graph[i][j] = col / row_sum
    graph = {i: dict(row) for i, row in graph.items()}

    return graph, names


if __name__ == "__main__":
    graph, names = create_graph()
    with open("cached.txt", "w") as f:
        f.write(str([graph, names]))
