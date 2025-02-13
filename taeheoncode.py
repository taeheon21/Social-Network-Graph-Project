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
            print("t")
            
    
    def find_friends(self, memeber):
        if member in self.graph:
            return self.graph[member]
        else:
            print('Member does not exist')
            return []
        
    def find_mutual_friends(self, member1, member2):
        if member1 not in self.graph or member2 not in self.graph:
            print('Member does not exist')
            return []
        else:
            return set(self.graph[member1].keys()) & set(self.graph[member2].keys())
        
    def suggest_friends(self, member):
        if member not in self.graph:
            return []
        
        friends = set(self.find_friends(member))
        suggestions = set()
        
        for friend in friends:
            mutuals = set(self.find_mutual_friends(member, friend))
            suggestions.update(mutuals- friends- {member})
            
        return suggestions
            
            
            
            
            
#Example
network = graph()

# Add members
network.add_member("Taeheon", 21, ["reading", "travelling"])

#Add relationships
network.add_relationship("Taeheon", "Sultan", weight=5)

# Find direct friends of Taeheon
print("Taeheon's friends:", network.find_friends("Taeheon"))


# Find mutual friends (Taeheon-sultan)
print("Mutual friends between Taeheon and Sultan:", network.find_mutual_friends("Taeheon", "Sultan"))





        


         
       
        
        
        
        
    
        
        
        

