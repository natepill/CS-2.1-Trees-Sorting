from collections import deque


class AVLNode(object):
    def __init__(self, data):
        '''initialize an AVL node object with its data'''
        self.data = data
        self.left = None
        self.right = None
        self.height = 0


    def is_leaf(self):
        '''return a boolean indicating whether this node is a leaf'''
        return self.left is None and self.right is None

    def is_branch(self):
        '''return a boolean indicating whether this node is a branch'''
        return not self.is_leaf()

    def has_left(self):
        '''return a boolean indicating whether this node has a left child'''
        return self.left is not None

    def has_right(self):
        '''return a boolean indicating whether this node has a right child'''
        return self.right is not None

    def update_height(self):
        '''update the nodes height based on the heights of its children'''
        if self.is_leaf():
            self.height = 0
        elif not self.has_left():
            self.height = self.right.height + 1
        elif not self.has_right():
            self.height = self.left.height + 1
        else:
            if self.left.height > self.right.height:
                self.height = self.left.height + 1
            else:
                self.height = self.right.height + 1

    def balance_factor(self):
        '''return an integer indicating the balance factor of this node'''
        if self.is_leaf():
            return 0
        elif not self.has_right():
            return -self.left.height - 1
        elif not self.has_left():
            return self.right.height + 1
        else:
            return self.right.height - self.left.height

    def right_rotate(self):
        '''perform a right roation from this node and return the new root'''
        left_node = self.left
        self.left = left_node.right
        left_node.right = self
        self.update_height()
        left_node.update_height()
        return left_node

    def left_rotate(self):
        '''perform a left rotation from this node and return the new root'''
        right_node = self.right
        self.right = right_node.left
        right_node.left = self
        self.update_height()
        right_node.update_height()
        return right_node


class AVLTree(object):
    def __init__(self, items=None):
        '''initialize an AVL tree object with optional items'''
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def is_empty(self):
        '''return a boolean indicating if this tree is empty'''
        return self.root is None

    def insert(self, item, node=None):
        '''recursively insert a node in this tree, keeping track of its
        path and balancing each node on your way back up to the root'''
        # check if the tree is empty
        if self.is_empty():
            # if so add the first node as the root
            self.root = AVLNode(item)
            # increment size by 1
            self.size += 1
            # stop insertion
            return
        # check if node is none (first method call)
        if node is None:
            # if so start from the root
            node = self.root
            # increase the size by 1 (this only happens once per insertion)
            self.size += 1
        # if the item is equal to this nodes data
        if item == node.data:
            # the items  already exists in the tree, decrenent size by 1
            self.size -= 1
            # stop insertion
            return
        # otherwise if the item is less than the current node
        elif item < node.data:
            # check if there is something in the nodes left spot
            if node.has_left():
                # if so recursively call insert on that node and store its subtree
                new_subtree = self.insert(item, node.left)
                # check if a new subtree was returned by the insertion
                if new_subtree is not None:
                    # if so update its left child with the new subtree
                    node.left = new_subtree
            # otherwise (the node has no left child)
            else:
                # instantiate a new node object with item
                new_node = AVLNode(item)
                # add the new node to the left
                node.left = new_node
        # otherwise (the item is greater than the current node)
        else:
            # check if there is something in the nodes right spot
            if node.has_right():
                # if so recursively call insert on that node and store its subtree
                new_subtree = self.insert(item, node.right)
                # check if a new subtree was returned by the insertion
                if new_subtree is not None:
                    # if so update its left child with the new subtree
                    node.right = new_subtree
            # otherwise (the node has no right child))
            else:
                # instantiate a new node object with item
                new_node = AVLNode(item)
                # add the new node to the right
                node.right = new_node
        # update the weights of the node
        node.update_height()
        # balance the node's subtrees
        return self.balance(node)

    def balance(self, node):
        '''given a node, determine its balance factor and if it is above 1 or
        below -1 balance that subtree. return the new root or None if no balancing
        actions are necessary'''
        # get the node's balance factor
        balance_factor = node.balance_factor()
        # check if the node's subtree is balanced
        if abs(balance_factor) < 2:
            # if it is return nothing
            return None
        # check if the tree is skewed left
        if balance_factor < -1:
            # if item is less than the node.left
            if node.left.balance_factor() < 0:
                # left-left case
                new_root = node.right_rotate()
            else:  # item is greater than the node.left
                # left-right case
                node.left = node.left.left_rotate()
                new_root = node.right_rotate()
        else:  # balance factor is positive (tree skewed right)
            # if item is less than node.right.data
            if node.right.balance_factor() > 0:
                # right-right case,
                new_root = node.left_rotate()
            # if item is greater than the node.right.data
            else:
                # right-Left case
                node.right = node.right.right_rotate()
                new_root = node.left_rotate()
        # if the node is already our root
        if node is self.root:
            # update the root
            self.root = new_root
        # return the new root so the parent can update its child
        return new_root

    def items_in_order(self):
        '''return a list of items in order'''
        items = []
        print(items)
        if not self.is_empty():
            # traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # return in-order list of all items in tree
        return items

    def items_level_order(self):
        '''return a list of items in level order'''
        items = []
        if not self.is_empty():
            # traverse tree in-order from root, appending each node's item
            self._traverse_level_order(self.root, items.append)
        # return level-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        '''recursively traverse each node of this tree in order (DFS)
        calling a visit function on each node'''
        if node.has_left():
            self._traverse_in_order_recursive(node.left, visit)
        # visit this node's data with given function
        visit(node.data)
        # traverse right subtree, if it exists
        if node.has_right():
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_level_order(self, start_node, visit):
        '''Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.'''
        # create queue to store nodes not yet traversed in level-order
        queue = deque()
        # enqueue given starting node
        queue.append(start_node)
        # loop until queue is empty
        while len(queue) is not 0:
            # dequeue node at front of queue
            node = queue.popleft()
            # visit this node's data with given function
            visit(node.data)
            # enqueue this node's left child, if it exists
            if node.left is not None:
                queue.append(node.left)
            # enqueue this node's right child, if it exists
            if node.right is not None:
                queue.append(node.right)


if __name__ == '__main__':
    at = AVLTree([1, 7, 5, 8, 6, 15, 4])
    print(at.items_in_order())
