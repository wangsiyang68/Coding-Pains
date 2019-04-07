##hash function

class Hashtable:
    def __init__(self, length): 
        self._list = []
        self._length = length
        for i in range(0,length):
            self._list.append([None,[]])

    def Hash(self, string): #hash function
        total = 0
        for letter in str(string):
            total += ord(letter)
        hash_value = total%self._length
        return hash_value

    def insert(self, string): #insert function
        hash_value = self.Hash(string)
        if self._list[hash_value] == [None,[]]:
            self._list[hash_value] = [string,[]]
        else:
            self._list[hash_value][1].append(string)

##    def delete(self, string): #delete function
##        hash_value = Hash(string)
##        if self._list[hash_value][0] == string:
##            if len(self._list[hash_value[1])):
##                for string in self._list[hash_value][1]:
                    
    def get(self, hash_value):
        return self._list[hash_value][0]
    
    def __str__(self): #print function
       print(self._list)
       return ''

    
        
a = Hashtable(11)
print(a.Hash('NJC'))
a.insert('NJC')
a.insert('proud')
a.insert('to')
a.insert('be')
a.insert('service')
a.insert('with')
a.insert('honour')
a.insert('scholarship')
a.insert('creativity')
a.insert('loyalty')
a.insert('integrity')
print(a)
print(a.get(a.Hash('proud')))
