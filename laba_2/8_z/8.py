class Node:
    def __init__(self, key):
        self.key = key  #ключ узла
        self.left = None  #ссылка на левого ребенка
        self.right = None  #ссылка на правого ребенка

f = open('number8.txt', 'r')
lines = f.read().splitlines()  #считываем файл
f.close()

if len(lines) == 0: #файл пуст
    height = 0
else:
    n = int(lines[0]) #число вершин дерева
    if n == 0:
        height = 0
    else:
        nodes = [None] * (n + 1) #список для хранения узлов
        for i in range(1, n + 1): #создаем объекты узлов только с ключами
            parts = lines[i].split()
            key = int(parts[0])
            nodes[i] = Node(key)
        for i in range(1, n + 1): #устанавливаем ссылки на левого и правого ребенка
            parts = lines[i].split()
            left_index = int(parts[1])
            right_index = int(parts[2])
            if left_index != 0:
                nodes[i].left = nodes[left_index]
            if right_index != 0:
                nodes[i].right = nodes[right_index]

        # Теперь узел nodes[1] является корнем дерева
        def rec_height(node):
            if node is None:
                return 0
            left_height = rec_height(node.left)
            right_height = rec_height(node.right)
            # Высота текущего узла равна 1 плюс максимум из высот поддеревьев
            return 1 + (left_height if left_height > right_height else right_height)


        height = rec_height(nodes[1]) # Вычисляем высоту дерева, вызывая функцию для корня (узел с индексом 1)


f_output = open('number8.txt', 'w')
f_output.write(str(height))
f_output.close()
