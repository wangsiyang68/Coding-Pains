##Sorted Singly Linked List practice
##this is in ascending order

class Node:
    def __init__(self, data):
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

class SSLL:
    def __init__(self):
        self._root = None

    def insert(self, data):
        if self._root == None: #if there is nothing in the list
            self._root = Node(data)
        else:
            prev = self._root
            node = Node(data)
            if node.get_data() < prev.get_data():#if node is smaller than root
                node.set_next(prev)
                self._root = node
            else:
                while prev.get_next() and node.get_data() > prev.get_next().get_data(): #if there is a next node AND node is larger than prev.next:
                    prev = prev.get_next() #move to next node
                if prev.get_next():#if this is not the last node
                    node.set_next(prev.get_next())
                prev.set_next(node)

    def find(self, data):
        current = self._root
        while current != None and current.get_data() != data:
            current = current.get_next()
        return bool(current)

    def delete(self, data):
        if self._root == None: #if list is empty
            return False
        elif self._root.get_data() == data: #if the first node is correct
            self._root = self._root.get_next()
        else:
            prev = self._root
            while prev.get_next() and prev.get_next().get_data() != data: #if the next node is not empty and next node's data is not correct
                prev = prev.get_next()
            if prev: #if the node is found
                prev.set_next(prev.get_next().get_next())
            else: #if data does not exist
                return False

    def __str__(self):
        if self._root == None:
            return '[]'
        else:
            print('[', end = '')
            current = self._root
            while current != None:
                if current.get_next():
                    print(current.get_data(), end = ',')
                else:
                    print(current.get_data(), end = '')
                current = current.get_next()
            return ']'

lol = SSLL()
lol.insert(4)
lol.insert(0)
lol.insert(2)
lol.insert(9)
lol.insert(3)
lol.insert(5)
print(lol)
print(lol.find(9))
print(lol.find(0))
print(lol.find(2))
print(lol.find(4))
lol.delete(9)
lol.delete(2)
lol.delete(0)
print(lol)            
        
