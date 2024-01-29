import random
from load_data import load_data

graph, state_names = load_data()


def get_name(state):
    return state_names[state]


def get_likelihoods(state):
    return graph[state]


def get_next_state(state):
    likelihoods = get_likelihoods(state)
    random_number = random.random()

    cumulative_likelihood = 0
    for next_state, likelihood in likelihoods.items():
        cumulative_likelihood += likelihood
        if random_number < cumulative_likelihood:
            return next_state


# num_times_visited = {
#     "A": 0,
#     "B": 0,
#     "C": 0,
#     "D": 0,
#     "E": 0,
# }

# state = 1
# for _ in range(10000000):
#     name = get_name(state)
#     num_times_visited[name] += 1
#     state = get_next_state(state)

# print(num_times_visited)

state = state_names.index("LORD")
for _ in range(1000):
    print(get_name(state), end=" ")
    state = get_next_state(state)
