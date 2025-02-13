class graph:
    def __init__(self, directed = False):
        self.graph = {}
        self.directed = directed
        
    def add_member(self, member, age, interests):
        if member not in self.graph:
            self.graph[member] = {'age': age, 'interests': interests}
        else:
            print('Member already exists')
            
    def remove_member(self, member):
        if member in self.graph:
            del self.graph[member]
        else:
            print('Member does not exist')
    
    def addrelations ( self, mem1, mem2, weight =1): #add edges
        if mem1 in self.graph and mem2 in self.graph:
            i,j = self.graph [mem1], self.graph[mem2]
            self.matrix [i][j] =weight
            self.matrix [j][i] =weight
        else:
            print ( "Both members must be initialized as objects to form a relationship")
            
        


         
       
        
        
        
        
    
        
        
        

