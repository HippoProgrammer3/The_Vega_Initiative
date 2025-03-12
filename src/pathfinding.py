# Fully implemented by SuitablyMysterious - despite commit being from pygame port by HippoProgrammer

import heapq

class Node:
    def __init__(self, x, y, g=0, h=0):
        self.x = x
        self.y = y
        self.g = g  
        self.h = h  
        self.f = g + h  
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f  

def heuristic(a, b):
    """Uses Manhattan distance for grid-based movement."""
    return abs(a.x - b.x) + abs(a.y - b.y)

def astar(grid, start, goal):
    """Finds the shortest path from start (x1, y1) to goal (x2, y2)."""
    open_list = []
    closed_set = set()

    start_node = Node(*start)
    goal_node = Node(*goal)
    
    heapq.heappush(open_list, start_node)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  

    while open_list:
        current = heapq.heappop(open_list)

        if (current.x, current.y) == (goal_node.x, goal_node.y):
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]  

        closed_set.add((current.x, current.y))

        for dx, dy in directions:
            x, y = current.x + dx, current.y + dy

            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:  
                if (x, y) in closed_set:
                    continue

                neighbor = Node(x, y, current.g + 1, heuristic(Node(x, y), goal_node))
                neighbor.parent = current

                heapq.heappush(open_list, neighbor)

    return None  