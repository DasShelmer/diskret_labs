

class MTS:
    def __init__(self, egraph):
        self.verts = MTS.load_verts(egraph)
        self.egraph = egraph
        self.result = None
        self.run_kruskal()
        self.result = sorted(self.result, key=lambda i: i[:-1])

    # Алгоритм Краскала для нахождения минимального остовного дерева
    def run_kruskal(self):
        # Сортируем рёбра по возрастанию длин
        self.egraph = sorted(self.egraph, key=lambda e: e[2])

        # Соотносит вершины к множеству
        ranks = {}

        # Указывает главные вершины во множествах
        roots = {}

        # Строит множества с каждой вершиной
        for b in self.verts:
            roots[b] = b
            ranks[b] = 0

        i = 0  # Индекс рёбер для выборки
        e = 0  # Индекс рёбер для построения ответа
        result = []  # Ответ

        # В результате только может быть рёбер меньше чем вершин
        while e < len(self.verts) - 1:
            # Ищем множества у двух вершин
            a, b, weight = self.egraph[i]
            first = self.find_set(roots, a)
            second = self.find_set(roots, b)

            # Если добавление этого ребра не создаст цикла, то добавляем его в ответ
            if first != second:
                e += 1
                result.append([a, b, weight])
                self.make_set_union(roots, ranks, first, second)
            i += 1

        self.result = result

    # Вывод результата
    def print_result(self):
        full_weight = sum(item[2] for item in self.result)
        for a, b, weight in self.result:
            print(f'{a}--{b}  {weight}')
        print(full_weight)

    # Нахождение вершин из графа
    def load_verts(egraph):
        verts = set(v for i in egraph for v in i[:-1])
        return list(sorted(verts))

    # Ищет множество для узла
    def find_set(self, roots, node):
        if roots[node] == node:
            return node
        return self.find_set(roots, roots[node])

    # Объединяет множества
    def make_set_union(self, roots, rank, first, second):
        main_v_1 = self.find_set(roots, first)
        main_v_2 = self.find_set(roots, second)

        # Включаем множество меньшего ранга во множество большего ранга
        if rank[main_v_1] < rank[main_v_2]:
            roots[main_v_1] = main_v_2
        elif rank[main_v_1] > rank[main_v_2]:
            roots[main_v_2] = main_v_1
        else:
            # Случай одинаковых рангов, один ранг повышаем и включаем множество с меньшим
            roots[main_v_2] = main_v_1
            rank[main_v_1] += 1


primer46 = [
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

mts46 = MTS(primer46)
mts46.print_result()
# 1--2  2
# 1--3  3
# 3--7  1
# 4--5  1
# 5--7  0.5
# 6--7  1
# 6--8  2
# 10.5

zadacha41 = [
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

mts41 = MTS(zadacha41)
mts41.print_result()

# 1--4  2
# 10--11  4
# 2--3  2
# 3--4  2
# 4--5  3
# 4--6  3
# 6--7  2
# 7--8  3
# 8--9  3
# 9--11  4
# 28
