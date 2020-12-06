from typing import Any, List, Tuple


class MTSKruskal:
    def __init__(self, graph: List[Tuple[str, str, float]], sort_result=True):
        self.graph = graph
        self.vertices = self._get_vertices()
        self.result: List[Tuple[str, str, float]]
        self.kruskal()
        if sort_result:
            self.result = sorted(self.result, key=lambda i: i[:-1])

    def _get_vertices(self):
        # Создаём список вершин на основе рёбер графа.
        vertices = set(v for i in self.graph for v in i[:-1])
        return list(sorted(vertices))

    def find_parent(self, parent, node):
        """
        Нахождение множества для узла.
        """
        if parent[node] == node:
            return node
        return self.find_parent(parent, parent[node])

    def union(self, parent, rank, x, y):
        """
        Объединение подмножеств в множество.
        """
        xroot = self.find_parent(parent, x)
        yroot = self.find_parent(parent, y)

        # Объединяем множество с меньшим рангом с
        # множеством большего ранга.
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        # Если ранги одинаковые, то один из них повышам
        # и устанавливаем эл. как родительский.
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        """
        Функция для нахождения MST(Минимального остовного дерева).
        Алгоритм Краскала.
        """
        # Сортируем рёбра по возрастанию длин.
        self.graph = sorted(self.graph, key=lambda i: i[2])

        ei = 0
        ri = 0
        result = []
        parent = {}

        # Даёт обозначение, вершина-множество
        rank = {}

        # Заполняем подмножества по одному узлу.
        for node in self.vertices:
            parent[node] = node
            rank[node] = 0

        # Конечное кол-во рёбер должно быть на 1 меньше,
        # чем кол-во вершин.
        while ri < len(self.vertices)-1:
            # Берём наименьшее ребро и ищем циклы.
            u, v, w = self.graph[ei]
            ei += 1
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)

            # Если это ребро не создаёт цикла,
            # то включаем его в ответ и углубляемся.
            if x != y:
                ri += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        # Записываем ответ.
        self.result = result


ex46: Any = [
    ('1', '2', 2),
    ('1', '3', 3),
    ('1', '4', 4),
    ('2', '3', 5),
    ('2', '6', 3),
    ('3', '4', 1.6),
    ('3', '5', 1.2),
    ('3', '7', 1),
    ('4', '5', 1),
    ('5', '7', 0.5),
    ('6', '7', 1),
    ('6', '8', 2),
    ('7', '8', 2.5)
]

no41: Any = [
    ('1', '2', 3),
    ('1', '3', 3),
    ('1', '4', 2),
    ('1', '5', 4),
    ('2', '3', 2),
    ('2', '8', 4),
    ('3', '4', 2),
    ('3', '6', 4),
    ('3', '7', 5),
    ('4', '5', 3),
    ('4', '6', 3),
    ('5', '6', 4),
    ('5', '5', 10),
    ('6', '7', 2),
    ('6', '10', 5),
    ('7', '8', 3),
    ('7', '9', 4),
    ('7', '10', 6),
    ('7', '11', 7),
    ('8', '9', 3),
    ('9', '11', 4),
    ('10', '11', 4)
]

mts = MTSKruskal(no41)
cost = sum(item[2] for item in mts.result)
for u, v, weight in mts.result:
    print(f"{u}-{v}  ({weight})")
print(cost)
# ex46:
# 1-2  (2)
# 1-3  (3)
# 3-7  (1)
# 4-5  (1)
# 5-7  (0.5)
# 6-7  (1)
# 6-8  (2)
# 10.5

# no41:
# 1-4  (2)
# 10-11  (4)
# 2-3  (2)
# 3-4  (2)
# 4-5  (3)
# 4-6  (3)
# 6-7  (2)
# 7-8  (3)
# 8-9  (3)
# 9-11  (4)
# 28
