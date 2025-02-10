import networkx as nx
import matplotlib.pyplot as plt

# Список обласних центрів України
cities = [
    "Київ", "Львів", "Харків", "Одеса", "Дніпро", "Запоріжжя", "Вінниця", "Полтава", "Чернігів",
    "Суми", "Черкаси", "Хмельницький", "Тернопіль", "Івано-Франківськ", "Ужгород", "Луцьк", "Рівне",
    "Житомир", "Кропивницький", "Миколаїв", "Херсон", "Чернівці", "Донецьк", "Луганськ"
]

# Створення графа
G = nx.Graph()
G.add_nodes_from(cities)

# Додавання зв'язків між містами (умовні зв'язки для моделювання доріг)
edges = [
    ("Київ", "Житомир"), ("Київ", "Чернігів"), ("Київ", "Полтава"), ("Київ", "Черкаси"),
    ("Львів", "Рівне"), ("Львів", "Тернопіль"), ("Львів", "Івано-Франківськ"), ("Львів", "Ужгород"),
    ("Харків", "Суми"), ("Харків", "Полтава"), ("Харків", "Донецьк"), ("Харків", "Луганськ"),
    ("Одеса", "Миколаїв"), ("Одеса", "Вінниця"), ("Одеса", "Кропивницький"),
    ("Дніпро", "Запоріжжя"), ("Дніпро", "Полтава"), ("Дніпро", "Кропивницький"),
    ("Запоріжжя", "Донецьк"), ("Запоріжжя", "Херсон"),
    ("Вінниця", "Житомир"), ("Вінниця", "Хмельницький"), ("Вінниця", "Одеса"),
    ("Полтава", "Суми"),
    ("Черкаси", "Кропивницький"), ("Черкаси", "Дніпро"),
    ("Тернопіль", "Івано-Франківськ"), ("Тернопіль", "Хмельницький"),
    ("Івано-Франківськ", "Чернівці"),
    ("Ужгород", "Луцьк"),
    ("Рівне", "Житомир"), ("Рівне", "Луцьк"),
    ("Кропивницький", "Миколаїв"),
    ("Херсон", "Миколаїв"), ("Херсон", "Донецьк"),
    ("Чернівці", "Хмельницький")
]

G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(12, 8))
nx.draw(G, with_labels=True, node_size=1500, node_color="lightblue", font_size=10, edge_color="gray")
plt.title("Мережа автомобільних доріг між обласними центрами України")
plt.show()

# Аналіз характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_centrality = nx.degree_centrality(G)

print(f"Кількість міст (вершин): {num_nodes}")
print(f"Кількість доріг (ребер): {num_edges}")
print("Ступені вершин:")
for city, degree in G.degree():
    print(f"{city}: {degree}")

# Функції для пошуку шляху

def dfs_path(graph, start, goal, path=None):
    if path is None:
        path = []
    path.append(start)
    if start == goal:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_path = dfs_path(graph, neighbor, goal, path.copy())
            if new_path:
                return new_path
    return None


def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        vertex, path = queue.pop(0)
        for neighbor in graph.neighbors(vertex):
            if neighbor not in path:
                if neighbor == goal:
                    return path + [neighbor]
                queue.append((neighbor, path + [neighbor]))
    return None

# Тест DFS та BFS
start_city = "Київ"
goal_city = "Львів"
dfs_result = dfs_path(G, start_city, goal_city)
bfs_result = bfs_path(G, start_city, goal_city)

print("\nШлях DFS:", dfs_result)
print("Шлях BFS:", bfs_result)