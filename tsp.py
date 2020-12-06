import math
from typing import List
maxsize = float('inf')


class TSPBaB:
    def __init__(self, matrix: List[List[int]]) -> None:
        self.matrix = matrix
        self.n = len(matrix)  # размерность матрицы
        self.visited = [False] * self.n  # массив посещённости точек
        self.path_length = maxsize  # длина результирующего пути
        self.path = [-1] * (self.n + 1)  # результирующий путь
        self._curr_path = [-1] * (self.n+1)  # текущий путь
        self._curr_bound = 0.  # текущая оценка
        self._curr_weight = 0.  # текущая сумма
        self._curr_level = 1  # текущий уровень ветвления

        # Рассчитываем оценку для начального узла.
        for i in range(self.n):
            self._curr_bound += (self.first_min(i) + self.second_min(i))

        self._curr_bound = math.ceil(self._curr_bound / 2)

        # Начинаем с 0-го элемента.
        self.visited[0] = True
        self._curr_path[0] = 0

        # Запускаем алгоритм.
        self.TSPRecursive()

    def first_min(self, i):
        """
        Находит минимальную дугу с вершиной i.
        """
        min = maxsize
        for k in range(self.n):
            if self.matrix[i][k] < min and i != k:
                min = self.matrix[i][k]

        return min

    def second_min(self, i):
        """
        Находит две минимальных дуги с вершиной i и возвращает вторую.
        """
        first, second = maxsize, maxsize
        for j in range(self.n):
            if i == j:
                continue
            if self.matrix[i][j] <= first:
                second = first
                first = self.matrix[i][j]

            elif(self.matrix[i][j] <= second and self.matrix[i][j] != first):
                second = self.matrix[i][j]

        return second

    def TSPRecursive(self, curr_weight=0, level=1):
        """
        Решение задачи коммивояжера через метод ветвей и границ.
        """
        # Случай, когда мы прошли через все узлы.
        if level == self.n:

            # Проверяем наличие дуги из последнего узла в первый.
            if self.matrix[self._curr_path[level - 1]][self._curr_path[0]]:

                # Записываем всю длину пути и сравниваем её
                curr_res = curr_weight + self.matrix[self._curr_path[level - 1]][self._curr_path[0]]
                if curr_res < self.path_length:
                    self.path = self._curr_path.copy()
                    self.path[self.n] = self.path[0]
                    self.path_length = curr_res
            return

        # Для всех остальных случаев решаем задачу оптимизации
        # методом ветвей и границ.
        for i in range(self.n):
            # Проверяем не является ли текущий узел
            # посещённым или находящимся на диагонали.
            if self.matrix[self._curr_path[level-1]][i] and not self.visited[i]:
                old_curr_bound = self._curr_bound
                curr_weight += self.matrix[self._curr_path[level - 1]][i]

                # Вычисляем оценку, но для 1 уровня отдельно.
                if level == 1:
                    bound = (self.first_min(self._curr_path[level - 1]) + self.first_min(i)) / 2
                    self._curr_bound -= bound
                else:
                    bound = (self.second_min(self._curr_path[level - 1]) + self.first_min(i)) / 2
                    self._curr_bound -= bound

                # Проверяем текущую длину пути (self._curr_bound + curr_weight)
                # если она меньше предыдущей, то углубляемся.
                if self._curr_bound + curr_weight < self.path_length:
                    self._curr_path[level] = i
                    self.visited[i] = True

                    self.TSPRecursive(curr_weight, level + 1)

                # Если же нет, то откатываем изменения в значениях.
                curr_weight -= self.matrix[self._curr_path[level - 1]][i]
                self._curr_bound = old_curr_bound

                # Так же откатываем посещение узла.
                self.visited = [False] * len(self.visited)
                for j in range(level):
                    if self._curr_path[j] != -1:
                        self.visited[self._curr_path[j]] = True


def TSP(matrix):
    tsp = TSPBaB(matrix)

    print("Длина пути:", tsp.path_length)
    print("Путь:", '->'.join(str(tsp.path[i]+1) for i in range(tsp.n + 1)))


ex43 = [
    [0, 7, 2, 9, 7],
    [5, 0, 3, 9, 1],
    [4, 8, 0, 5, 3],
    [5, 6, 4, 0, 7],
    [7, 6, 3, 7, 0]]

# TSP(ex43)
# Длина пути: 21
# Путь: 1->2->5->3->4->1

no38 = [
    [0, 3, 6, 1, 4],
    [9, 0, 9, 3, 8],
    [7, 1, 0, 7, 5],
    [1, 4, 6, 0, 1],
    [2, 5, 1, 8, 0]]

# TSP(no38)
# Длина пути: 13
# Путь: 1->4->5->3->2->1
