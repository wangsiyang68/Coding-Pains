class Node: #Tree node: left and right child + data which can be any object
    def __init__(self,data):#Node constructor
        self.left = None
        self.right = None
        self.data = data

    def get_data(self):
        return self.data

    def set_data(self,data):
        self
    
    def insert(self, data):#Insert new node with data
        if self.data: #means bool(self.data) which will return true
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)

                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def lookup(self,data,parent = None): #lookup node containing data and information about the parent node
        if data < self.data:
            if self.left is None:
                return None, None 
            return self.left.lookup(data,self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data,self)
        else:
            return self,parent

    def children_count(self):
        cnt = 0
        if self.left:
            cnt+= 1
        if self.right:
            cnt+= 1
        return cnt
    
    def delete(self,data):#delete node containing data
        node, parent = self.lookup(data)#lookup the address of the data first
        if node is not None:
            children_count = node.children_count()
        if children_count == 0:#if node has no children, just remove it
            if parent:#actually why need to if parent
                if parent.left is node:
                    parent.left = None #why don't you just say node = None
                else:
                    parent.right = None
                del node
            else:
                self.data = None
        elif children_count == 1:
            if node.left:
                n = node.left
            else:
                n = node.right
            if parent:
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
                del node
            else:
                self.left = n.left
                self.right = n.right
                self.data = n.data
        else:#if node has 2 children
            parent = node
                
        
