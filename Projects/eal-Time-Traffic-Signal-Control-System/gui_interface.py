import pygame
import sys
from traffic_model import CityGrid

# Initialize PyGame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)

# Screen dimensions
GRID_SIZE = 100
MARGIN = 20
STATS_HEIGHT = 100

class TrafficGUI:
    def __init__(self, city):
        self.city = city
        self.width = len(city.grid)
        self.height = len(city.grid[0])
        
        # Calculate window size
        window_width = self.width * GRID_SIZE + (self.width + 1) * MARGIN
        window_height = self.height * GRID_SIZE + (self.height + 1) * MARGIN + STATS_HEIGHT
        
        self.screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Adaptive Traffic Light Control")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 16)
        
    def draw_intersection(self, x, y, intersection):
        pos_x = MARGIN + x * (GRID_SIZE + MARGIN)
        pos_y = MARGIN + y * (GRID_SIZE + MARGIN)
        
        # Draw intersection background
        pygame.draw.rect(self.screen, GRAY, (pos_x, pos_y, GRID_SIZE, GRID_SIZE))
        
        # Draw traffic light
        if intersection.current_light == "NS":
            pygame.draw.circle(self.screen, GREEN, (pos_x + 30, pos_y + 30), 10)
            pygame.draw.circle(self.screen, RED, (pos_x + 70, pos_y + 30), 10)
            pygame.draw.circle(self.screen, RED, (pos_x + 30, pos_y + 70), 10)
            pygame.draw.circle(self.screen, GREEN, (pos_x + 70, pos_y + 70), 10)
        else:  # "EW"
            pygame.draw.circle(self.screen, RED, (pos_x + 30, pos_y + 30), 10)
            pygame.draw.circle(self.screen, GREEN, (pos_x + 70, pos_y + 30), 10)
            pygame.draw.circle(self.screen, GREEN, (pos_x + 30, pos_y + 70), 10)
            pygame.draw.circle(self.screen, RED, (pos_x + 70, pos_y + 70), 10)
        
        # Draw queue counts
        queues = intersection.get_queue_counts()
        for i, (dir, count) in enumerate(queues.items()):
            text = self.font.render(f"{dir}:{count}", True, WHITE)
            if dir == "N":
                self.screen.blit(text, (pos_x + 40, pos_y + 10))
            elif dir == "S":
                self.screen.blit(text, (pos_x + 40, pos_y + GRID_SIZE - 20))
            elif dir == "E":
                self.screen.blit(text, (pos_x + GRID_SIZE - 30, pos_y + 40))
            elif dir == "W":
                self.screen.blit(text, (pos_x + 10, pos_y + 40))
    
    def draw_stats(self, step, total_waiting):
        stats_y = self.height * (GRID_SIZE + MARGIN) + MARGIN
        
        # Background
        pygame.draw.rect(self.screen, BLACK, (0, stats_y, self.screen.get_width(), STATS_HEIGHT))
        
        # Texts
        step_text = self.font.render(f"Step: {step}", True, WHITE)
        waiting_text = self.font.render(f"Total waiting cars: {total_waiting}", True, WHITE)
        
        self.screen.blit(step_text, (20, stats_y + 20))
        self.screen.blit(waiting_text, (20, stats_y + 50))
    
    def update(self, step, total_waiting):
        self.screen.fill(BLACK)
        
        # Draw grid
        for x in range(self.width):
            for y in range(self.height):
                self.draw_intersection(x, y, self.city.grid[x][y])
        
        # Draw stats
        self.draw_stats(step, total_waiting)
        
        pygame.display.flip()
        self.clock.tick(1)  # 1 frame per second
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()