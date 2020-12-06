from queue import PriorityQueue
from typing import Any, Dict, List, Optional, Set, Tuple
maxsize = float('inf')

class DijkstraPriorQ:
    def __init__(self, graph: Dict[str, Set[Tuple[str, Any]]], src: str, dist: str):
        self.graph: Dict[str, Set[Tuple[str, float]]] = graph
        self.length = 0.
        self.path: List[str] = []
        self.run_dijkstra(src, dist)

    def run_dijkstra(self, src: str, dist: str):
        """
        Алгоритм Дейкстры c приоритетной очередью.
        """
        visited = set()
        length: Dict[str, float] = {src: 0}
        parent: Dict[str, Optional[str]] = {src: None}
        queue: PriorityQueue = PriorityQueue()

        queue.put((0, src))
        while queue:
            while not queue.empty():
                # Находим ближайший узел и проверяем его на посещённость.
                vertex = queue.get()[1]
                if vertex not in visited:
                    break
            else:
                # Если все узлы в очереди закончились, то завершаем алг.
                break
            visited.add(vertex)
            # Если узел целевой, то завершаем алг.
            if vertex == dist:
                break
            # Рассчитываем пути до приоритетных узлов.
            for neighbor, distance in self.graph[vertex]:
                # Посещённые пропускаем.
                if neighbor in visited:
                    continue
                old_length = length.get(neighbor, maxsize)
                new_length = length[vertex] + distance
                # Сравниваем старый самый короткий путь и
                # новый, если новый короче, то углубляемся.
                if new_length < old_length:
                    queue.put((new_length, neighbor))
                    length[neighbor] = new_length
                    parent[neighbor] = vertex

        # Строим обратный путь.
        if dist not in parent:
            return None
        v: Optional[str] = dist
        path = []
        while v is not None:
            path.append(v)
            v = parent[v]
        # Инвертируем путь.
        self.path = path[::-1]
        self.length = length[dist]


ex45 = {
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

# dij = DijkstraPriorQ(ex45, '1', '11')
# print(dij.path)
# print(dij.length)
# ['1', '4', '6', '10', '11']
# 14


no40 = {
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

dij = DijkstraPriorQ(no40, '1', '10')
# print(dij.path)
# print(dij.length)
# ['1', '2', '6', '9', '10']
# 16
