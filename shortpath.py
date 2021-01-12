from queue import PriorityQueue


class ShortPath:
    def __init__(self, tgraph, start, end):
        self.tgraph = tgraph
        self.result_length = 0.0
        self.result_path = []
        self.run_dijkstra(start, end)

    def print_result(self):
        print('-'.join(self.result_path), f'  {self.result_length}')

    def run_dijkstra(self, start, end):
        visited = set()  # Посещённые вершины
        length = {start: 0}  # Длины между вершинами и конечной вершиной
        root = {start: None}  # Связь вершин (сами рёбра)
        queue: PriorityQueue = PriorityQueue()

        queue.put((0, start))
        while queue:
            while not queue.empty():
                # Получаем ближайшую вершину
                vertex = queue.get()[1]
                # Если она была посещена, то выходим из цикла
                if vertex not in visited:
                    break
            else:
                # Если в очереди не осталось узлов для рассмотрения, то выходим из цикла
                break
            # Указываем текущую вершину как посещённую
            visited.add(vertex)
            # Если вершина конечная, то алгоритм сработал
            if vertex == end:
                break
            # Рассчитываем пути до ключевых вершин на пути
            for neariest, distance in self.tgraph[vertex]:
                # Пропускаем посещённые вершины
                if neariest in visited:
                    continue
                prev_len = length.get(neariest, float('inf'))
                current_len = length[vertex] + distance
                # Выбираем кратчайший путь и продолжаем идти по нему,
                # добавив его последний узел в очередь
                if current_len < prev_len:
                    queue.put((current_len, neariest))
                    length[neariest] = current_len
                    root[neariest] = vertex

        self.result_length = length[end]
        # Выстраиваем путь в обратном направлении
        if end not in root:
            return None
        vert = end
        inv_path = []
        while vert is not None:
            inv_path.append(vert)
            vert = root[vert]
        # Переставляем путь в правильное направление
        self.result_path = inv_path[::-1]


primer45 = {
    '1': {('2', 1), ('3', 5), ('4', 4)},
    '2': {('1', 1), ('5', 7)},
    '3': {('1', 5), ('5', 2), ('6', 6), ('7', 2)},
    '4': {('1', 4), ('6', 3), ('7', 8)},
    '5': {('2', 7), ('3', 2), ('8', 7), ('9', 8)},
    '6': {('3', 6), ('4', 3), ('9', 7), ('10', 3)},
    '7': {('3', 2), ('4', 8), ('9', 4), ('10', 6)},
    '8': {('5', 7), ('11', 5)},
    '9': {('5', 8), ('6', 7), ('7', 4), ('11', 5)},
    '10': {('6', 3), ('7', 6), ('11', 4)},
    '11': {('8', 5), ('9', 5), ('10', 4)}
}

sp45 = ShortPath(primer45, '1', '11')
sp45.print_result()
# 1-4-6-10-11   14


zadacha40 = {
    '1': {('2', 2), ('3', 4), ('4', 3)},
    '2': {('1', 2), ('5', 6), ('6', 2)},
    '3': {('1', 4), ('5', 8), ('6', 2), ('7', 7)},
    '4': {('1', 3), ('5', 6), ('6', 1), ('7', 8)},
    '5': {('2', 6), ('3', 8), ('4', 6), ('8', 7), ('9', 8)},
    '6': {('2', 2), ('3', 2), ('4', 1), ('8', 6), ('9', 4)},
    '7': {('3', 7), ('4', 8), ('8', 3), ('9', 3)},
    '8': {('5', 7), ('6', 6), ('7', 3), ('10', 9)},
    '9': {('5', 8), ('6', 4), ('7', 3), ('10', 8)}
}

sp40 = ShortPath(zadacha40, '1', '10')
sp40.print_result()
# 1-2-6-9-10   16
