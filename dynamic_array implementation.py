import ctypes

class DynamicArray():
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.makearray(self.capacity)
        
    def __len__(self):
        return self.n
    
    def __getitem__(self , k):
        if not 0 <= k < self.capacity:
            return IndexError("Index out of range")
        return self.A[k]
    
    def append(self , elle):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
            
        self.A[self.n] = elle
        self.n += 1
        
    def resize(self , size):
        B = self.makearray(size)
        
        for i in range(self.n):
            B[i] = self.A[i]
            
        self.A = self.B
        self.capacity = size
        
    def makearray(self , size):
        return (size * ctypes.py_object)()
        