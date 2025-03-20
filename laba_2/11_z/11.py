class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node
        elif key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._get_min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        if node is None:
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def exists(self, key):
        return self._exists(self.root, key)

    def _exists(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._exists(node.left, key)
        else:
            return self._exists(node.right, key)

    def next(self, key):
        result = None
        node = self.root
        while node:
            if node.key > key:
                result = node
                node = node.left
            else:
                node = node.right
        return result.key if result else "none"

    def prev(self, key):
        result = None
        node = self.root
        while node:
            if node.key < key:
                result = node
                node = node.right
            else:
                node = node.left
        return result.key if result else "none"

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y


    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self._get_min_value_node(node.left)

tree = AVLTree()
output = []

with open("input.txt", "r") as input_file:
    input_lines = input_file.readlines()

for line in input_lines:
    parts = line.strip().split()
    if not parts:
        continue
    cmd = parts[0]
    if cmd == "insert":
        x = int(parts[1])
        tree.insert(x)
    elif cmd == "delete":
        x = int(parts[1])
        tree.delete(x)
    elif cmd == "exists":
        x = int(parts[1])
        output.append("true" if tree.exists(x) else "false")
    elif cmd == "next":
        x = int(parts[1])
        output.append(str(tree.next(x)))
    elif cmd == "prev":
        x = int(parts[1])
        output.append(str(tree.prev(x)))

with open("output.txt", "w") as output_file:
    for line in output:
        output_file.write(line + "\n")
