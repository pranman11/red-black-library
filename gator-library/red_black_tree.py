
class RedBlackNode:
        
    def __init__(self, data):
        self.data = data
        self.key = data.book_id if data else 0
        self.color = 1    # new node to be inserted will always be red, 0 = black, 1 = red
        self.parent = None
        self.left = None
        self.right = None

    def get_key(self):
        return self.key

    def set_color(self, tree, color):
        if color == "black":
            if self.color != 0:
                tree.color_flip_count += 1
                self.color = 0
        else:
            if self.color != 1:
                tree.color_flip_count += 1
                self.color = 1
        

    def get_color(self) -> str:
        return "red" if self.color else "black"

class RedBlackTree:
    def __init__(self) -> None:
        self.LEAF = RedBlackNode(None)
        self.LEAF.color = 0    # black node
        self.LEAF.left = None
        self.LEAF.right = None
        self.root = self.LEAF
        self.color_flip_count = 0

    def inorder(self, node):
        if node==None:
            return
        self.inorder(node.left)
        print(node.key)
        self.inorder(node.right)

    def insert(self, new_data):
        new_node = RedBlackNode(new_data)  # create a new red node
        new_node.parent = None
        new_node.left = self.LEAF
        new_node.right = self.LEAF

        curr_node = self.root
        curr_node_parent = None        

        # traverse the tree to find the right position for node
        while curr_node != self.LEAF:
            curr_node_parent = curr_node
            if new_node.get_key() == curr_node.get_key():
                return -1
            elif new_node.get_key() < curr_node.get_key():
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        
        # once the insertion point is found, check whether node will be left or right node
        new_node.parent = curr_node_parent
        if curr_node_parent is None:
            self.root = new_node
        elif new_node.get_key() < curr_node_parent.get_key():
            curr_node_parent.left = new_node
        else:
            curr_node_parent.right = new_node

        if new_node.parent is None:
            new_node.set_color(self, "black")
            return

        if new_node.parent.parent is None:
            return
        self.balance_after_insert(new_node)
        

    def search_tree(self, node, key):
        if not node or key == node.get_key():
            return node

        if key < node.get_key():
            return self.search_tree(node.left, key)
        return self.search_tree(node.right, key)
    
    def search(self, key):
        return self.search_tree(self.root, key)

    def balance_after_insert(self, node) -> None:
        while node.parent.get_color() == "red":
            if node.parent.parent and node.parent == node.parent.parent.right:
                parents_sibling = node.parent.parent.left
                if parents_sibling.get_color() == "red":
                    parents_sibling.set_color(self, "black")
                    if parents_sibling.parent: parents_sibling.parent.set_color(self, "black")
                    if parents_sibling.parent.parent: parents_sibling.parent.parent.set_color(self, "red")
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.set_color(self, "black")
                    node.parent.parent.set_color(self, "red")
                    self.left_rotate(node.parent.parent)
            else:
                if node.parent.parent: parents_sibling = node.parent.parent.right

                if parents_sibling.get_color() == "red":
                    parents_sibling.set_color(self, "black")
                    node.parent.set_color(self, "black")
                    if node.parent.parent: node.parent.parent.set_color(self, "red")
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.set_color(self, "black")
                    if node.parent.parent: 
                        node.parent.parent.set_color(self, "red")
                        self.right_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.set_color(self, "black")


    def left_rotate(self, node) -> None:
        node_right = node.right
        node.right = node_right.left
        if node_right.left != self.LEAF:
            node_right.left.parent = node

        node_right.parent = node.parent
        if node.parent is None:
            self.root = node_right
        elif node == node.parent.left:
            node.parent.left = node_right
        else:
            node.parent.right = node_right
        node_right.left = node
        node.parent = node_right

    def right_rotate(self, node) -> None:
        node_left = node.left
        node.left = node_left.right
        if node_left.right != self.LEAF:
            node_left.right.parent = node

        node_left.parent = node.parent
        if node.parent is None:
            self.root = node_left
        elif node == node.parent.right:
            node.parent.right = node_left
        else:
            node.parent.left = node_left
        node_left.right = node
        node.parent = node_left

    def minimum(self, node):
        while node.left != self.LEAF:
            node = node.left
        return node

    # Function to fix issues after deletion
    def balance_after_delete(self, node):
        # Repeat until node reaches all nodes and color of node is black
        while node != self.root and node.get_color() == "black":
            if node == node.parent.left:
                sibling = node.parent.right
                # if sibling is red
                if sibling.get_color() == "red":
                    sibling.set_color(self, "black")
                    node.parent.set_color(self, "red")
                    self.left_rotate(node.parent)
                    sibling = node.parent.right
                # if both the child are black
                if sibling.left.get_color() == "black" and sibling.right.get_color() == "black":
                    sibling.set_color(self, "red")
                    node = node.parent
                else:
                    if sibling.right.get_color() == "black":
                        # if right child of s is black, set left child of s as black, call right rotation on x
                        sibling.left.set_color(self, "black")
                        sibling.set_color(self, "red")
                        self.right_rotate(sibling)
                        sibling = node.parent.right

                    sibling.set_color(self, node.parent.get_color())
                    # Set parent of node as black
                    node.parent.set_color(self, "black")             
                    sibling.right.set_color(self, "black") 

                    self.left_rotate(node.parent)
                    node = self.root
            else:
                # If node is right child of its parent
                sibling = node.parent.left
                if sibling.get_color() == "red":
                    sibling.set_color(self, "black")
                    node.parent.set_color(self, "red") 
                    self.right_rotate(node.parent)
                    sibling = node.parent.left

                if sibling.right.get_color() == "black" and sibling.right.get_color() == "black":
                    sibling.set_color(self, "red") 
                    node = node.parent
                else:
                    # If left child of sibling is black
                    if sibling.left.get_color() == "black":
                        # set right child of sibling as black
                        sibling.right.set_color(self, "black") 
                        sibling.set_color(self, "red") 
                        self.left_rotate(sibling)
                        sibling = node.parent.left

                    sibling.set_color(self, node.parent.get_color())
                    node.parent.set_color(self, "black")
                    sibling.left.set_color(self, "black")
                    self.right_rotate(node.parent)
                    node = self.root
        node.set_color(self, "black")

    # swapping nodes
    def swap(self, node1, node2) :
        if node1.parent == None:
            self.root = node2
        elif node1 == node1.parent.left:
            node1.parent.left = node2
        else:
            node1.parent.right = node2
        node2.parent = node1.parent

    # helper to delete node
    def delete_node(self, node, key):
        curr_node = self.LEAF
        # traverse the tree to find node to be deleted
        while node != self.LEAF:
            if node.get_key() == key:
                curr_node = node
            if node.get_key() <= key:
                node = node.right
            else:
                node = node.left

        # if we have reached a leaf node, then key has not been found
        if curr_node == self.LEAF:
            return "Node to deleted not found"

        target_node = curr_node
        target_node_original_color = target_node.color
        # If left child of node to be deleted is NULL, store right child of that node in x 
        # and swap right child with node to be deleted
        if curr_node.left == self.LEAF:
            x = curr_node.right
            self.swap(curr_node, curr_node.right)
        # If rigt child of node to be deleted is NULL, store left child of that node in x 
        # and swap left child with node to be deleted
        elif curr_node.right == self.LEAF:
            x = curr_node.left
            self.swap(curr_node, curr_node.left)
        # node to be deleted has both right and left children, find min of right subtree
        else:
            target_node = self.minimum(curr_node.right)
            target_node_original_color = target_node.color
            x = target_node.right
            if target_node.parent == curr_node:
                x.parent = target_node
            else :
                self.swap(target_node,target_node.right)
                target_node.right = curr_node.right
                target_node.right.parent = target_node

            self.swap(curr_node, target_node)
            target_node.left = curr_node.left
            target_node.left.parent = target_node
            target_node.color = curr_node.color
            self.color_flip_count += 1
        # If color of target node is black then tree is unbalanced
        if target_node_original_color == 0:
            self.balance_after_delete(x)
        
        return curr_node.data


    # Entry point for deleting a key from RB tree
    def delete(self, key):
        return self.delete_node(self.root, key)
    
    def search_tree_between(self, query_value1, query_value2, node, list_of_nodes=[]):
        if node == self.LEAF:
            return list_of_nodes
        list_of_nodes = self.search_tree_between(query_value1, query_value2, node.left, list_of_nodes)
        if node.get_key() >= query_value1 and node.get_key() <= query_value2:
            list_of_nodes.append(node.data)
        return self.search_tree_between(query_value1, query_value2, node.right, list_of_nodes)

    def search_between(self, query_value1, query_value2):
        return self.search_tree_between(query_value1, query_value2, self.root, [])

    def search_closest_node(self, node, min_distance_nodes, query_value):
        if node == self.LEAF:
            return min_distance_nodes
        curr_min_distance = 999999 if len(min_distance_nodes) == 0 else abs(min_distance_nodes[0].book_id - query_value)
        distance = abs(node.get_key() - query_value)
        if distance == 0:
            return [node.data]
        if distance == curr_min_distance:
            min_distance_nodes.append(node.data)
        if distance < curr_min_distance:
            min_distance_nodes = [node.data]
        if query_value - node.get_key() < 0:
            return self.search_closest_node(node.left, min_distance_nodes, query_value)
        return self.search_closest_node(node.right, min_distance_nodes, query_value)
    
    def search_closest(self, query_value):
        if self.root.left == self.LEAF and self.root.right == self.LEAF:
            return [self.root.data]
        return self.search_closest_node(self.root, [], query_value)
