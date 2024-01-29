# graph = [
#     [0.0, 1 / 3, 1 / 3, 1 / 3, 0.0],
#     [1 / 4, 0.0, 1 / 4, 1 / 4, 1 / 4],
#     [1 / 2, 1 / 2, 0.0, 0.0, 0.0],
#     [1 / 2, 1 / 2, 0.0, 0.0, 0.0],
#     [0.0, 1.0, 0.0, 0.0, 0.0],
# ]

# state_names = [
#     "A",
#     "B",
#     "C",
#     "D",
#     "E",
# ]


# graph = [
#     [0.2, 0.8],
#     [0.1, 0.9],
# ]

# state_names = [
#     "Sunny",
#     "Rainy",
# ]


def load_data():
    with open("cached.txt") as f:
        return eval(f.read())
