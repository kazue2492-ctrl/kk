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

# --- Pygame эхлүүлэлт ---
def init_game():
     """
     # Функцийн зорилго:
    PyGame-ийг эхлүүлж, тоглоомын үндсэн дэлгэц, clock үүсгэх.

    # Хэрхэн хийх:
    1. pygame.init() дуудаж PyGame-ийн бүх дэд модулиудыг эхлүүлэх.
    2. pygame.display.set_mode((WIDTH, HEIGHT)) ашиглаж тоглоомын дэлгэцийг үүсгэх.
       - WIDTH, HEIGHT нь дэлгэцийн өргөн, өндөр.
    3. pygame.display.set_caption("Snake Game") дуудаж цонхны гарчгийг тохируулах.
    4. pygame.time.Clock() ашиглаж тоглоомын frame rate-ийг хянах Clock үүсгэх.
    5. screen болон clock обьектуудыг буцаах, ингэснээр үндсэн game loop-д ашиглах боломжтой болно.
    """


# --- Pure functions ---
def random_position():
     """
    # Зорилго:
    Хоолны шинэ байрлал үүсгэх.

    # Алхам алхмаар хийх:
    1. WIDTH болон HEIGHT-г CELL_SIZE-ээр хуваарилаж random координат үүсгэх.
    2. (x, y) tuple буцаах.
    """
     
def move_snake(snake, direction):
     """
    # Зорилго:
    Snake-ийн толгойг хөдөлгөж шинэ list үүсгэх.

    # Алхам алхмаар хийх:
    1. Толгойны координатыг авах (snake[0]).
    2. Direction-д үндэслэн шинэ толгойг тооцоолох.
    3. Шинэ толгойг list-ийн эхэнд нэмэх.
    4. Сүүл хэсгийг хасах (snake[:-1]).
    5. Шинэ snake list-ийг буцаах.
    """

def grow_snake(snake):
    """
    # Тухайн функц хийх зүйлс:
    - Snake-ийн сүүл хэсгийг давхарлаад нэмэх
    - Өссөн snake list-ийг буцаах
    """

def check_food(snake, food):
    """
    # Тухайн функц хийх зүйлс:
    - Snake-ийн толгой food-той ижил координат дээр байгаа эсэхийг шалгах
    - True/False буцаах
    """

def check_collision(snake):
    """
    # Тухайн функц хийх зүйлс:
    - Snake өөрийн бие дээр мөргөсөн эсэхийг шалгах
    - Snake дэлгэцийн хилээс гарсан эсэхийг шалгах
    - Collision болсон эсэхийг True/False буцаах
    """

def update_snake(snake, direction, food):
   """
    # Тухайн функц хийх зүйлс:
    - move_snake-ийг дуудна
    - check_food ашиглан хоол идсэн бол grow_snake дуудна
    - Хоол идсэн бол food-г шинэ байрлалд гаргана
    - Шинэ snake болон food-ийг буцаах
    """

# --- Render функцууд ---
def draw_snake(screen, snake):
     """
    # Тухайн функц хийх зүйлс:
    - map функц ашиглан snake-ийн бүх segment-г дэлгэц дээр зурна
    """

def draw_food(screen, food):
    """
    # Тухайн функц хийх зүйлс:
    - Snake-ийн food-г дэлгэц дээр зурна
    """

def draw_score(screen, snake):
    """
    # Тухайн функц хийх зүйлс:
    - reduce ашиглан snake-ийн уртыг тоолно
    - Оноог дэлгэц дээр харуулах
    """

# --- Main loop ---
def main():
    """
    # Тухайн функц хийх зүйлс:
    - init_game() → screen, clock-ийг үүсгэх
    - Анхны snake, direction, food-г тодорхойлох
    - Game loop:
        - Event-үүдийг шалгах (pygame.event.get())
        - Direction update (reduce ашиглаж FP маягаар)
        - Collision шалгах
        - Snake + Food update (update_snake функц)
        - Дэлгэцийг цэвэрлэх
        - draw_snake, draw_food, draw_score дуудлага
        - pygame.display.flip() болон clock.tick(FPS)
    - pygame.quit() дуудлага
    """

if __name__ == "__main__":
    main()