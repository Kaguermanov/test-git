import random

class Ship:
    def __init__(self, points):
        self.points = points

class Board:
    def __init__(self, ships):
        self.ships = ships
        self.board = [[' ' for _ in range(6)] for _ in range(6)]
        self.shot_cells = set()

    def place_ships(self):
        for ship in self.ships:
            for point in ship.points:
                x, y = point
                self.board[x][y] = 'S'

    def display_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def check_shot(self, x, y):
        if (x, y) in self.shot_cells:
            raise ValueError("Вы уже стреляли в эту клетку!")
        self.shot_cells.add((x, y))

        for ship in self.ships:
            if (x, y) in ship.points:
                ship.points.remove((x, y))
                self.board[x][y] = 'X'
                if not ship.points:
                    print("Корабль потоплен!")
                else:
                    print("Корабль подбит!")
                return True

        self.board[x][y] = 'O'
        print("Промах!")
        return False

def generate_random_ship_points(length):
    x = random.randint(0, 6)
    y = random.randint(0, 6)
    direction = random.choice(['horizontal', 'vertical'])

    ship_points = [(x, y)]

    for _ in range(1, length):
        if direction == 'horizontal':
            x += 1
        else:
            y += 1
        ship_points.append((x, y))

    return ship_points

def generate_ships():
    ships = []
    for length in [3, 2, 2, 1, 1, 1, 1]:
        ship_points = generate_random_ship_points(length)
        new_ship = Ship(ship_points)
        ships.append(new_ship)
    return ships

def main():
    player_ships = generate_ships()
    computer_ships = generate_ships()

    player_board = Board(player_ships)
    computer_board = Board(computer_ships)

    player_board.place_ships()

    while any(ship.points for ship in computer_ships):
        print("Ваша доска:")
        player_board.display_board()

        try:
            x = int(input("Введите номер строки (0-6): "))
            y = int(input("Введите номер столбца (0-6): "))
        except ValueError:
            print("Ошибка! Введите числа.")
            continue

        if 0 <= x <= 6 and 0 <= y <= 6:
            result = computer_board.check_shot(x, y)
            if not result:
                computer_x = random.randint(0, 6)
                computer_y = random.randint(0, 6)
                player_result = player_board.check_shot(computer_x, computer_y)

    print("Игра завершена!")

if __name__ == "__main__":
    main()
