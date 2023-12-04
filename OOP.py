class Ship:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.hits = set()

    def is_hit(self, coordinate):
        return coordinate in self.coordinates

    def take_hit(self, coordinate):
        self.hits.add(coordinate)

    def is_sunk(self):
        return set(self.coordinates) == self.hits


class Board:
    def __init__(self, ships):
        self.ships = ships
        self.board = [['О' for _ in range(6)] for _ in range(6)]
        self.shots = set()

    def print_board(self):
        print("  | 1 | 2 | 3 | 4 | 5 | 6 |")
        for i, row in enumerate(self.board, start=1):
            print(f"{i} | {' | '.join(row)} |")

    def place_ships(self):
        for ship in self.ships:
            for coordinate in ship.coordinates:
                row, col = coordinate
                self.board[row][col] = '■'

    def record_shot(self, coordinate):
        if coordinate in self.shots:
            raise ValueError("Вы уже стреляли в эту клетку.")
        self.shots.add(coordinate)

    def apply_shot_result(self, coordinate, is_hit):
        row, col = coordinate
        if is_hit:
            self.board[row][col] = 'X'
        else:
            self.board[row][col] = 'T'

    def is_all_ships_sunk(self):
        return all(ship.is_sunk() for ship in self.ships)


import random

def generate_random_coordinates(size, num_ships):
    coordinates = set()
    while len(coordinates) < num_ships:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        coordinates.add((row, col))
    return coordinates

def generate_ships():
    ships = []

    # 1 корабль на 3 клетки
    ships.append(Ship(generate_random_coordinates(6, 3)))

    # 2 корабля на 2 клетки
    for _ in range(2):
        ships.append(Ship(generate_random_coordinates(6, 2)))

    # 4 корабля на одну клетку
    for _ in range(4):
        ships.append(Ship(generate_random_coordinates(6, 1)))

    return ships

def main():
    player_ships = generate_ships()
    computer_ships = generate_ships()

    player_board = Board(player_ships)
    computer_board = Board(computer_ships)

    player_board.place_ships()
    computer_board.place_ships()

    while True:
        print("Ваша доска:")
        player_board.print_board()
        print("\nДоска компьютера:")
        computer_board.print_board()

        try:
            user_input = input("Введите координаты выстрела (например, A3): ").upper()
            if len(user_input) != 2 or not user_input[0].isalpha() or not user_input[1].isdigit():
                raise ValueError("Некорректный ввод. Введите в формате A3, B4 и т.д.")

            row = int(user_input[1]) - 1
            col = ord(user_input[0]) - ord('A')

            player_board.record_shot((row, col))

            if (row, col) in [coordinate for ship in computer_ships for coordinate in ship.coordinates]:
                print("Попадание!")
                for ship in computer_ships:
                    if (row, col) in ship.coordinates:
                        ship.take_hit((row, col))
                        if ship.is_sunk():
                            print("Корабль потоплен!")
                            if computer_board.is_all_ships_sunk():
                                print("Вы победили!")
                                return
                player_board.apply_shot_result((row, col), True)
            else:
                print("Промах!")
                player_board.apply_shot_result((row, col), False)

            # Ход компьютера
            computer_row = random.randint(0, 5)
            computer_col = random.randint(0, 5)

            computer_board.record_shot((computer_row, computer_col))

            if (computer_row, computer_col) in [coordinate for ship in player_ships for coordinate in ship.coordinates]:
                print("Компьютер попал в ваш корабль!")
                for ship in player_ships:
                    if (computer_row, computer_col) in ship.coordinates:
                        ship.take_hit((computer_row, computer_col))
                        if ship.is_sunk():
                            print("Ваш корабль потоплен!")
                            if player_board.is_all_ships_sunk():
                                print("Компьютер победил!")
                                return
                computer_board.apply_shot_result((computer_row, computer_col), True)
            else:
                print("Компьютер промахнулся!")
                computer_board.apply_shot_result((computer_row, computer_col), False)

        except ValueError as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()



