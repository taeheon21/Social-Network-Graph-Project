import random
import numpy as np
from collections import deque


class graph:

    def __init__(self, size, directed=False):
        self.graph = {}
        self.matrix = np.zeros((size, size), dtype=int)
        self.directed = directed

    def add_member(self, member, age, interests):
        if member not in self.graph:
            self.graph[member] = {'age': age, 'interests': interests, 'friends': {}}
        else:
            print('Member already exists')

    def remove_member(self, member):
        if member in self.graph:
            del self.graph[member]
        else:
            print('Member does not exist')

    def add_relationship(self, member1, member2, weight=1):
        if member1 in self.graph and member2 in self.graph:
            self.graph[member1]['friends'][member2] = weight
            if not self.directed:
                self.graph[member2]['friends'][member1] = weight
        else:
            print('One or both members do not exist')

    def remove_relationship(self, member1, member2):
        if member1 in self.graph and member2 in self.graph:
            if member2 in self.graph[member1]['friends']:
                del self.graph[member1]['friends'][member2]
            if not self.directed and member1 in self.graph[member2]['friends']:
                del self.graph[member2]['friends'][member1]
        else:
            print('One or both members do not exist')

    def find_friends(self, member):
        if member in self.graph:
            return list(self.graph[member]['friends'].keys())
        else:
            print('Member does not exist')
            return []

    def find_mutual_friends(self, member1, member2):
        if member1 not in self.graph or member2 not in self.graph:
            print('Member does not exist')
            return []
        else:
            return set(self.graph[member1]['friends'].keys()) & set(self.graph[member2]['friends'].keys())

    def suggest_friends(self, member):
        if member not in self.graph:
            return []

        friends = set(self.find_friends(member))
        suggestions = set()

        for friend in friends:
            mutuals = set(self.find_mutual_friends(member, friend))
            suggestions.update(mutuals - friends - {member})

        return suggestions

    def shortest_path(self, member1, member2):

        if member1 not in self.graph or member2 not in self.graph:
            print("One or both members do not exist.")
            return [], 0

        queue = deque([(member1, [member1])])
        visited = set()

        while queue:
            current_member, path = queue.popleft()

            if current_member == member2:
                return path, len(path) - 1

            visited.add(current_member)

            for neighbor in self.graph[current_member]['friends']:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        return [], 0
def most_connected ( self):
    biggest_weight = 0
    for i in self.matrix :
        if i> biggest_weight
        biggest_weight = i

    return biggest_weight

# Example
network = graph(size=10)

# Add members
network.add_member("Taeheon", 21, ["reading", "travelling"])
network.add_member("Sultan", 22, ["sports", "music"])

# Add relationships
network.add_relationship("Taeheon", "Sultan", weight=5)

# Find direct friends of Taeheon
print("Taeheon's friends:", network.find_friends("Taeheon"))

# Find mutual friends (Taeheon-Sultan)
print("Mutual friends between Taeheon and Sultan:", network.find_mutual_friends("Taeheon", "Sultan"))

# Find shortest path between Taeheon and Sultan
path, degrees = network.shortest_path("Taeheon", "Sultan")
print("Shortest path between Taeheon and Sultan:", path, "with degrees of separation:", degrees)
