from get_key import wait, clear_console, get_key

from map import Map
from snake import Snake
from apple import Apple

#map - nowy  obiekt
my_map = Map(10, 10, ' ')

#snake - nowy obiekt
my_snake = Snake(my_map.size_x, my_map.size_y, 5, 5)

#apple - nwy obiekt
my_apple = Apple(my_map.size_x, my_map.size_y)

#socre - int zaczyna się od 0
score = 0

my_get_key = get_key()

while True:
    # wyczyść ekran
    clear_console()
    # wyczyść mapę
    my_map.clean()

    #pobierz wciśnięty klawisz
    my_key = my_get_key()

    # zmien kierunek węża na podstawie wcisnnietego klawisza
    # jak ESC to wyjdź z gry
    if my_key == 299: # w lewo
        my_snake.direction.x = -1
        my_snake.direction.y = 0
    elif my_key == 301: # w prawo
        my_snake.direction.x = 1
        my_snake.direction.y = 0
    elif my_key == 296: # w gore
        my_snake.direction.x = 0
        my_snake.direction.y = -1
    elif my_key == 304: # w dol
        my_snake.direction.x = 0
        my_snake.direction.y = 1
    elif my_key == 27:  # ESC
        break

    #sprawdz czy snake zjadł jabłko
        #jeżeli tak to zwiększ snake
               #i dodaj punkt i wylosuj w nowym miejscu jabłko
    if my_snake.body[0].x == my_apple.x and my_snake.body[0].y == my_apple.y:
        my_snake.add()
        my_apple.set_new_place()
        score += 1

    #snake idzie dalej
    my_snake.move()

    # sprwadz czy zjadł ogon:
        #jeżeli tak to GMAE OVER
    is_game_over = False
    for snake_i in range(1, len(my_snake.body)):
        if my_snake.body[0].x == my_snake.body[snake_i].x and my_snake.body[0].y == my_snake.body[snake_i].y:
            clear_console()
            print('GAME OVER! Wciśnij ESC aby wyjść.')
            is_game_over = True

    if is_game_over:
        break

    #  umieść jabło na mapie
    my_map.put_point(my_apple)

    #  umieść snake na mapie
    for snake_point in my_snake.body:
        my_map.put_point(snake_point)



    # wypisz na ekeranie mapę
    my_map.print()
    print(f'Liczba punktów {score}')
    wait()






