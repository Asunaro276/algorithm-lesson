class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
            return

        def _insert(node: Node, value: int) -> Node:
            if node is None:
                return Node(value)

            if node.value < value:
                node.right = _insert(node.right, value)
            else:
                node.left = _insert(node.left, value)
            return node
        _insert(self.root, value)

    def inorder(self) -> None:
        def _inorder(node: Node) -> None:
            if node is not None:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)
        _inorder(self.root)

    def search(self, value: int) -> bool:
        def _search(node: Node, value: int) -> bool:
            if node is None:
                return False

            if node.value == value:
                return True
            elif node.value > value:
                return _search(node.left, value)
            elif node.value < value:
                return _search(node.right, value)
        return _search(self.root, value)

    def min_val(self, node: Node) -> Node:
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def remove(self, value: int) -> None:
        def _remove(node: Node, value: int) -> Node:
            if node is None:
                return node

            if node.value > value:
                node.left = _remove(node.left, value)
            elif node.value < value:
                node.right = _remove(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                tmp = self.min_val(node.right)
                node.value = tmp.value
                node.right = _remove(node.right, tmp.value)
            return node
        _remove(self.root, value)


if __name__ == "__main__":
    bst = BST()
    bst.insert(5)
    bst.insert(10)
    bst.insert(3)
    bst.insert(1)
    bst.insert(4)
    bst.insert(6)
    bst.insert(11)
    bst.insert(12)
    bst.inorder()
    bst.remove(5)
    bst.inorder()
