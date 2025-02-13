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

    def add_relationship(self, mem1, mem2, weight=None):
        """Add a relationship between two members."""
        if mem1 in self.graph and mem2 in self.graph:
            if weight is None:
                weight = random.randint(1, 10)  # Assign a random weight if not provided

            # Update dictionary-based graph
            self.graph[mem1]['friends'][mem2] = weight
            if not self.directed:
                self.graph[mem2]['friends'][mem1] = weight
        else:
            print("Both members must be added first")

    def remove_relationship(self, mem1, mem2):
        """Remove a relationship between two members."""
        if mem1 in self.graph and mem2 in self.graph:
            self.graph[mem1]['friends'].pop(mem2, None)
            if not self.directed:
                self.graph[mem2]['friends'].pop(mem1, None)
        else:
            print("Both members must exist in the graph")

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
    def most_connected(self):
        biggest_weight = 0
        most_connected_member = None

        for member in self.graph:
            total_weight = sum(self.graph[member]['friends'].values())
            if total_weight > biggest_weight:
                biggest_weight = total_weight
                most_connected_member = member

        return most_connected_member, biggest_weight
        

# Example
network = graph(size=10)

# Add members
network.add_member("Taeheon", 21, ["reading", "travelling"])
network.add_member("Sultan", 22, ["sports", "music"])

# Add relationships
network.add_relationship("Taeheon", "Sultan")

# Find direct friends of Taeheon
print("Taeheon's friends:", network.find_friends("Taeheon"))

# Find mutual friends (Taeheon-Sultan)
print("Mutual friends between Taeheon and Sultan:", network.find_mutual_friends("Taeheon", "Sultan"))

# Find shortest path between Taeheon and Sultan
path, degrees = network.shortest_path("Taeheon", "Sultan")
print("Shortest path between Taeheon and Sultan:", path, "with degrees of separation:", degrees)

# Most connected members
print("Most connected members:", network.most_connected())
