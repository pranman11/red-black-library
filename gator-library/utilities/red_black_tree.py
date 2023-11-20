
class RedBlackNode:
        
    def __init__(self, data) -> None:
        self.data = data
        self.key = data.book_id
        self.color = 1    # 0 = black, 1 = red
        self.parent = None
        self.left = None
        self.right = None

    def get_key(self):
        return self.key

    def set_color(self, color):
        self.color = 0 if color == "black" else 1

    def get_color(self) -> str:
        return "red" if self.color else "black"

class RedBlackTree:
    def __init__(self) -> None:
        self.root = None
        self.color_flip_count = 0

    def insert(self, data):
        # create a node with red color and no parent and children

        if self.root == None:
            self.root = RedBlackNode(data)
            return

        node = RedBlackNode(data)
        print(self.root)
        curr_node = self.root
        curr_node_parent = None

        # traverse the tree to find the right position for node
        while not curr_node:
            curr_node_parent = curr_node
            if node.get_key() == curr_node.get_key():
                return -1
            elif node.get_key() < curr_node.get_key():
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        
        # once the insertion point is found, check whether node will be left or right node
        node.parent = curr_node_parent
        if curr_node_parent is None:
            self.root = node
        elif node.get_key() < curr_node_parent.get_key():
            curr_node_parent.left = node
        else:
            curr_node_parent.right = node

        if node.parent is None:
            node.set_color("black")
            return

        if node.parent.parent is None:
            return

        self.balance_after_insert()
        

    def balance_after_insert(self, node) -> None:
        while node.parent.get_color() == "red":
            if node.parent == node.parent.parent.right:
                parents_sibling = node.parent.parent.left
                if parents_sibling.is_red():
                    parents_sibling.set_color("black")
                    parents_sibling.parent.set_color("black")
                    parents_sibling.parent.parent.set_color("red")
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.set_color("black")
                    node.parent.parent.set_color("red")
                    self.left_rotate(node.parent.parent)
            else:
                parents_sibling = node.parent.parent.right

                if parents_sibling.is_red():
                    parents_sibling.set_color("black")
                    node.parent.set_color("black")
                    node.parent.parent.set_color("red")
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.set_color("black")
                    node.parent.parent.set_color("red")
                    self.right_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.set_color("black")


    def left_rotate(self, x) -> None:
        y = x.right
        x.right = y.left
        if not y.left.is_null():
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x) -> None:
        y = x.left
        x.left = y.right
        if not y.right.is_null():
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y