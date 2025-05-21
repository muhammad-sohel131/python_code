from collections import deque

def simulate_queue_change(queues, new_light):
    # Simulate what happens if we change the light
    new_queues = queues.copy()
    if new_light == "NS":
        new_queues["N"] = max(0, queues["N"] - 2)  # Let 2 cars pass
        new_queues["S"] = max(0, queues["S"] - 2)
    else:
        new_queues["E"] = max(0, queues["E"] - 2)
        new_queues["W"] = max(0, queues["W"] - 2)
    return new_queues

def evaluate_state(queues):
    # Lower score = better (fewer waiting cars)
    return queues["N"] + queues["S"] + queues["E"] + queues["W"]

def bfs_evaluate(intersection, depth=3):
    queue = deque()
    initial_state = (intersection.current_light, intersection.get_queue_counts(), 0)
    queue.append(initial_state)
    best_score = float('inf')
    best_action = None
    
    while queue:
        current_light, queues, current_depth = queue.popleft()
        
        if current_depth == depth:
            current_score = evaluate_state(queues)
            if current_score < best_score:
                best_score = current_score
                best_action = current_light
            continue
            
        # Try both possible light changes
        for next_light in ["NS", "EW"]:
            if next_light != current_light:
                new_queues = simulate_queue_change(queues, next_light)
                queue.append((next_light, new_queues, current_depth + 1))
    
    return best_action if best_action else intersection.current_light