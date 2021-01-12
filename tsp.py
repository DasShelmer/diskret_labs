import math


class TSP:
    def __init__(self, mgraph) -> None:
        self.mgraph = mgraph
        self.n = len(mgraph)  # размерность матрицы
        self.visited = [False] * self.n  # массив посещённости точек
        self.result_length = float('inf')  # длина результирующего пути
        self.result_path = [-1] * (self.n + 1)  # результирующий путь
        self._curr_path = [-1] * (self.n+1)  # текущий путь
        self._curr_bound = 0.0  # текущая оценка
        self._curr_weight = 0.0  # текущая сумма
        self._curr_level = 1  # текущий уровень ветвления

        # Рассчитываем оценку для первой вершины
        for i in range(self.n):
            self._curr_bound += (self.first_min(i) + self.second_min(i))

        self._curr_bound = math.ceil(self._curr_bound / 2)

        # Начинаем с 0-го элемента.
        self.visited[0] = True
        self._curr_path[0] = 0

        # Запускаем алгоритм.
        self.BranchAndBoundTSP()

    # Поиск кратчайшего ребра для вершины
    def first_min(self, vert):
        min = float('inf')
        for k in range(self.n):
            if self.mgraph[vert][k] < min and vert != k:
                min = self.mgraph[vert][k]

        return min

    # Поиск второй самой кратчайшей дуги для вершины
    def second_min(self, vert):
        first, second = float('inf'), float('inf')
        for j in range(self.n):
            if vert == j:
                continue
            if self.mgraph[vert][j] <= first:
                second = first
                first = self.mgraph[vert][j]

            elif(self.mgraph[vert][j] <= second and self.mgraph[vert][j] != first):
                second = self.mgraph[vert][j]

        return second

    # Метод ветвей и границ
    def BranchAndBoundTSP(self, curr_weight=0, level=1):
        # Случай, когда мы прошли через все узлы.
        if level == self.n:

            # Проверяем наличие дуги из последнего узла в первый.
            if self.mgraph[self._curr_path[level - 1]][self._curr_path[0]]:

                # Записываем всю длину пути и сравниваем её
                curr_res = curr_weight + self.mgraph[self._curr_path[level - 1]][self._curr_path[0]]
                if curr_res < self.result_length:
                    self.result_path = self._curr_path.copy()
                    self.result_path[self.n] = self.result_path[0]
                    self.result_length = curr_res
            return

        # Для всех остальных случаев решаем задачу оптимизации
        # методом ветвей и границ.
        for i in range(self.n):
            # Проверяем не является ли текущий узел
            # посещённым или находящимся на диагонали.
            if self.mgraph[self._curr_path[level-1]][i] and not self.visited[i]:
                old_curr_bound = self._curr_bound
                curr_weight += self.mgraph[self._curr_path[level - 1]][i]

                # Вычисляем оценку, но для 1 уровня отдельно.
                if level == 1:
                    bound = (self.first_min(self._curr_path[level - 1]) + self.first_min(i)) / 2
                    self._curr_bound -= bound
                else:
                    bound = (self.second_min(self._curr_path[level - 1]) + self.first_min(i)) / 2
                    self._curr_bound -= bound

                # Проверяем текущую длину пути (self._curr_bound + curr_weight)
                # если она меньше предыдущей, то углубляемся.
                if self._curr_bound + curr_weight < self.result_length:
                    self._curr_path[level] = i
                    self.visited[i] = True

                    self.BranchAndBoundTSP(curr_weight, level + 1)

                # Если же нет, то откатываем изменения в значениях.
                curr_weight -= self.mgraph[self._curr_path[level - 1]][i]
                self._curr_bound = old_curr_bound

                # Так же откатываем посещение узла.
                self.visited = [False] * len(self.visited)
                for j in range(level):
                    if self._curr_path[j] != -1:
                        self.visited[self._curr_path[j]] = True


def TSP(matrix):
    tsp = TSP(matrix)

    print("Длина пути:", tsp.path_length)
    print("Путь:", '->'.join(str(tsp.path[i]+1) for i in range(tsp.n + 1)))


ex43 = [
    [0, 7, 2, 9, 7],
    [5, 0, 3, 9, 1],
    [4, 8, 0, 5, 3],
    [5, 6, 4, 0, 7],
    [7, 6, 3, 7, 0]]

TSP(ex43)
# Длина пути: 21
# Путь: 1->2->5->3->4->1

no38 = [
    [0, 3, 6, 1, 4],
    [9, 0, 9, 3, 8],
    [7, 1, 0, 7, 5],
    [1, 4, 6, 0, 1],
    [2, 5, 1, 8, 0]]

TSP(no38)
# Длина пути: 13
# Путь: 1->4->5->3->2->1
