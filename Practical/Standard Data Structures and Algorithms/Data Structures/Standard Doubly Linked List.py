##standard doubly linked list
##note: always ask for node as an input for set next, set prev and insert

class Node:
    def __init__(self, data = None):
        self._data = data
        self._next = None
        self._prev = None

    def get_next(self):
        return self._next

    def set_next(self, node):
        self._next = node

    def get_prev(self):
        return self._prev

    def set_prev(self, node):
        self._prev = node

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

class dll:
    def __init__(self):
        self._root = None

    def insert(self, node):
        if self._root == None:
            self._root = node
        else:
            current = self._root
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(node)
            node.set_prev(current)

    def find(self, data):
        if self._root == None:
            return False
        else:
            current = self._root
            while current != None and current.get_data() != data:
                current = current.get_next()
            if current:
                return True
            else:
                return False

    def delete(self,data):
        if a.find(data) == False:
            return False
        else:
            current = self._root
            while current != None and current.get_data() != data:
                current = current.get_next()
            if current == self._root:
                current.get_next().set_prev(None)
                self._root = current.get_next()
                current.set_next(None)
            elif current.get_next() == None:
                current.get_prev().set_next(None)
                current.set_prev(None)
            else:
                current.get_prev().set_next(current.get_next())
                current.get_next().set_prev(current.get_prev())
                current.set_prev(None)
                current.set_next(None)

    def __str__(self):
        if self._root == None:
            return '[]'
        else:
            print('[', end = '')
            current = self._root
            while current.get_next() != None:
                print(current.get_data(), end = ',')
                current = current.get_next()
            print(current.get_data(), end = ']')

        return ''

a = dll()
a.insert(Node(1))
a.insert(Node(9))
a.insert(Node(0))
a.insert(Node(4))
a.insert(Node(3))
print(a)
print(a.find(1))
print(a.find(6))
a.delete(0)
print(a)
a.delete(1)
print(a)
a.delete(3)
print(a)
