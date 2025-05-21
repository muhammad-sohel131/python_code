from traffic_model import CityGrid
from bfs_decision import bfs_evaluate
from gui_interface import TrafficGUI

def calculate_total_waiting(city):
    total = 0
    for row in city.grid:
        for intersection in row:
            queues = intersection.get_queue_counts()
            total += sum(queues.values())
    return total

def main():
    city = CityGrid(width=3, height=3)  # 3x3 grid
    gui = TrafficGUI(city)
    
    for step in range(50):  # Simulate 50 steps
        city.generate_traffic()
        
        # Update traffic lights using BFS
        for row in city.grid:
            for intersection in row:
                best_light = bfs_evaluate(intersection)
                intersection.current_light = best_light
        
        total_waiting = calculate_total_waiting(city)
        gui.update(step, total_waiting)
        gui.handle_events()
        
        city.time += 1

if __name__ == "__main__":
    main()