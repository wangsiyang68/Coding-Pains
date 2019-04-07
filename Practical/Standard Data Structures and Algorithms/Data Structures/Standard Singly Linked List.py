##STANDARD singly linked list
class Node:
    def __init__(self, data = None):
        self._data = data
        self._next = None
        
    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_next(self):
        return self._next

    def set_next(self, node):
        self._next = node

class Sll:
    def __init__(self):
        self._root = None

    def insert(self, data):
        if self._root == None:
            self._root = Node(data)
        else:
            current = self._root
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(Node(data))
            
    def find(self, data):
        if self._root == None:
            return False
        else:
            current = self._root
            while current != None and current.get_data() != data:
                current = current.get_next()
            if current == None:
                return False
            else:
                return True

    def delete(self, data):
        if self._root == None:
            return False
        else:
            current = self._root
            while current.get_next() != None and current.get_next().get_data() != data:
                current = current.get_next()
            if current.get_next() == None:
                return False
            else:
                current.set_next(current.get_next().get_next())

    def __str__(self):
        current = self._root
        print('[', end = '')
        while current != None:
            if current.get_next():
                print(current.get_data(),end = ',')
            else:
                print(current.get_data(),end ='')
            current = current.get_next()
        return ']'
    
lol = Sll()
lol.insert(4)
lol.insert(0)
lol.insert(2)
lol.insert(9)
print(lol)
print(lol.find(9))
print(lol.find(0))
print(lol.find(2))
print(lol.find(4))
lol.delete(9)
print(lol)
