import sys
import time
import tracemalloc

# Увеличиваем лимит рекурсии, чтобы избежать ошибки при больших значениях
sys.setrecursionlimit(10**7)

def checkBST(node_index, min_val, max_val, nodes):
    """
    Свойство BST: min_val < key < max_val
    """
    if node_index == 0:
        # 0 означает, что ребёнка нет = пустое поддерево корректно
        return True

    # Индексы вершин в условии начинаются с 1, а в nodes с 0
    key, left_child, right_child = nodes[node_index - 1]

    # Проверяем, что текущий ключ в диапазоне
    if not (min_val < key < max_val):
        return False

    # Рекурсивно проверяем левое и правое поддерево
    return (checkBST(left_child, min_val, key, nodes) and checkBST(right_child, key, max_val, nodes))

def solve():
    tracemalloc.start()          # Начинаем отслеживать память
    start_time = time.time()     # Засекаем время

    # Считываем данные из input.txt
    with open("input.txt", "r") as fin:
        data = fin.read().strip().split()

    N = int(data[0])  # Число вершин

    # Случай пустого дерева
    if N == 0:
        # Пустое дерево по условию BST
        with open("output.txt", "w") as fout:
            fout.write("YES\n")

        # Замеряем и выводим время/память
        end_time = time.time()
        _, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Время работы: {end_time - start_time:.5f} сек.")
        print(f"Общее пиковое потребление памяти: {peak_memory / 1024:.3f} KB")
        return

    # Считываем вершины (K_i, L_i, R_i)
    nodes = []
    idx = 1
    for _ in range(N):
        K = int(data[idx])
        L = int(data[idx + 1])
        R = int(data[idx + 2])
        idx += 3
        nodes.append((K, L, R))

    # Проверяем свойство BST, корень - вершина с индексом 1
    # От минус беск, до плюс беск
    is_bst = checkBST(1, float("-inf"), float("inf"), nodes)

    # Записываем результат
    with open("output.txt", "w") as fout:
        if is_bst:
            fout.write("YES")
        else:
            fout.write("NO")

    # Замеряем и выводим время/память
    end_time = time.time()
    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Время работы: {end_time - start_time:.5f} сек.")
    print(f"Пиковое потребление памяти: {peak_memory / 1024:.3f} KB")

solve()
