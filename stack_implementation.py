class Stack():
    
    def __init__(self):
        self.item = []
        self.n = 0
        
    def push(self , value):
        self.item.append(value)
        self.n+= 1
        
    def pop(self):
        value = self.item[self.n - 1]
        del self.item[self.n - 1]
        self.n-= 1
        return value
        
    def peek(self):
        return self.item[self.n]
    
    def isEmpty(self):
        return self.n == 0
    
    def size(self):
        return self.n
        