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
            
        


         
       
        
        
        
        
    
        
        
        