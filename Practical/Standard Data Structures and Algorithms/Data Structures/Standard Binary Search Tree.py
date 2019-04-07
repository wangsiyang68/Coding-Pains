##Task 4
class Node:
    def __init__(self, data):
        self._left = None
        self._right = None
        self._data = data

    def get_data(self):
        return self._data

    def set_data(self,data):
        self._data = Node(data)
    
    def get_left(self):
        return self._left

    def set_left(self,data):
        self._left = Node(data)

    def get_right(self):
        return self._right

    def set_right(self,data):
        self._right = Node(data)

    def inorder(self):
        if self._left:
            self._left.inorder()
        print(self._data),
        if self._right:
            self._right.inorder()

class bst:
    def __init__(self):
        self._root = None

    def insert(self,data):
        if self._root == None:
            self._root = Node(data)
            return True
        else:
            current = self._root
            while current:
                if current.get_data() > data:
                    if current.get_left() == None:
                        current.set_left(data)
                        return True #acts as a break
                    current = current.get_left()
                else:
                    if current.get_right() == None:
                        current.set_right(data)
                        return True
                    current = current.get_right()
            return False

##    def delete    


    def inorder(self):
        if self._root == None:
            return None
        else:
            self._root.inorder()

tree = bst()
tree.insert(19)
tree.insert(6)
tree.insert(45)
tree.insert(4)
tree.insert(7)
tree.insert(33)
tree.insert(23)
tree.insert(9)
tree.insert(13)
print('inorder')
tree.inorder()
##print('preorder')
##tree.preorder()
##print('postorder')
##tree.postorder()
