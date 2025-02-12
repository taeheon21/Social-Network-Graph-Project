class graph(object):
    def __init__(self,nodes,edges):
        self.nodes=nodes
        self.edges=edges

    def add_member(self, member, age, interests):
        self.nodes[member]=[age,interests]
        
    def add_relation(self, member1, member2, relation):
        self.edges[(member1,member2)]=relation
        
        
    
        
        
        