import random

class Intersection:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.north_queue = []  # Cars coming from North
        self.south_queue = []  # Cars coming from South
        self.east_queue = []   # Cars coming from East
        self.west_queue = []   # Cars coming from West
        self.current_light = "NS"  # "NS" = North-South Green, "EW" = East-West Green

    def add_vehicle(self, direction):
        if direction == "N":
            self.north_queue.append(1)
        elif direction == "S":
            self.south_queue.append(1)
        elif direction == "E":
            self.east_queue.append(1)
        elif direction == "W":
            self.west_queue.append(1)

    def get_queue_counts(self):
        return {
            "N": len(self.north_queue),
            "S": len(self.south_queue),
            "E": len(self.east_queue),
            "W": len(self.west_queue)
        }

class CityGrid:
    def __init__(self, width=3, height=3):
        self.grid = [[Intersection(x, y) for y in range(height)] for x in range(width)]
        self.time = 0

    def generate_traffic(self):
        for row in self.grid:
            for intersection in row:
                if random.random() < 0.2:  # 20% chance of a new car
                    direction = random.choice(["N", "S", "E", "W"])
                    intersection.add_vehicle(direction)