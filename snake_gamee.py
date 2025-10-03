import snake_game
import random
from functools import reduce

# --- Тоглоомын тохиргоо ---
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

# --- Өнгө ---
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
WHITE = (255, 255, 255)

# --- Pygame эхлүүлэлт ---
def init_game():
    pygame.init()
    pygame.font.init()   # font модулийг бас эхлүүлнэ
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    return screen, clock

# --- Pure functions ---
def random_position():
    x = random.randrange(0, WIDTH, CELL_SIZE)
    y = random.randrange(0, HEIGHT, CELL_SIZE)
    return (x, y)

def move_snake(snake, direction):
    head_x, head_y = snake[0]
    if direction == "UP":
        new_head = (head_x, head_y - CELL_SIZE)
    elif direction == "DOWN":
        new_head = (head_x, head_y + CELL_SIZE)
    elif direction == "LEFT":
        new_head = (head_x - CELL_SIZE, head_y)
    elif direction == "RIGHT":
        new_head = (head_x + CELL_SIZE, head_y)
    else:
        new_head = (head_x, head_y)

    return [new_head] + snake[:-1]

def grow_snake(snake):
    return snake + [snake[-1]]

def check_food(snake, food):
    return snake[0] == food

def check_collision(snake):
    head_x, head_y = snake[0]
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        return True
    if snake[0] in snake[1:]:
        return True
    return False

def update_snake(snake, direction, food):
    new_snake = move_snake(snake, direction)
    if check_food(new_snake, food):
        new_snake = grow_snake(new_snake)
        food = random_position()
    return new_snake, food

# --- Render функцууд ---
def draw_snake(screen, snake):
    list(map(lambda segment: pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE)), snake))

def draw_food(screen, food):
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

def draw_score(screen, snake):
    score = reduce(lambda acc, _: acc + 1, snake, 0)
    font = pygame.font.SysFont(None, 30)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

# --- Main loop ---
def main():
    screen, clock = init_game()

    snake = [(100, 100), (80, 100), (60, 100)]
    direction = "RIGHT"
    food = random_position()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                direction = reduce(
                    lambda d, e: (
                        "UP" if e.key == pygame.K_UP and d != "DOWN" else
                        "DOWN" if e.key == pygame.K_DOWN and d != "UP" else
                        "LEFT" if e.key == pygame.K_LEFT and d != "RIGHT" else
                        "RIGHT" if e.key == pygame.K_RIGHT and d != "LEFT" else d
                    ),
                    [event], direction
                )

        if check_collision(snake):
            running = False

        snake, food = update_snake(snake, direction, food)

        screen.fill(BLACK)
        draw_snake(screen, snake)
        draw_food(screen, food)
        draw_score(screen, snake)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()