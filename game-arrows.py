import random
from itertools import chain


class GameArrows:
	def __init__(self):
		self.SIZE = None
		self.SYMBOLS = {'left': '←', 'right': '→', 'up': '↑', 'down': '↓', '.': '\u00B7'}
		self.DIRECTIONS = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}

	def create_field(self):
		grid = []
		for _ in range(self.SIZE):
			line = [None for _ in range(self.SIZE)]
			grid.append(line)
		return grid

	def draw_field(self, grid):
		f_line = '\t' + '\t'.join([str(num) for num in range(1, self.SIZE + 1)])
		print(f_line)
		for idx, line in enumerate(grid, 1):
			print('\t'.join([str(idx)] + line))

	def path_is_clear(self, grid, row, col, direction):
		action = [int(row) - 1, int(col) - 1]
		while True:
			action[0] = action[0] + int(self.DIRECTIONS[direction][0])
			action[1] = action[1] + int(self.DIRECTIONS[direction][1])
			if (-1 < action[0] < self.SIZE) and (-1 < action[1] < self.SIZE):
				if grid[action[0]][action[1]] != '\u00B7':
					return False
			else:
				break
		return True

	def make_move(self, grid, row, col, direction):
		row_idx = int(row) - 1
		col_idx = int(col) - 1
		if not ((-1 < row_idx < self.SIZE) and (-1 < col_idx < self.SIZE)):
			print('Такой клетки нет\n')
			return None
		elif grid[row_idx][col_idx] == '\u00B7':
			print('В этой клетке нет стрелки\n')
			return None
		elif grid[row_idx][col_idx] != self.SYMBOLS[direction]:
			print('Неверное направление\n')
			return None
		elif not self.path_is_clear(grid, row, col, direction):
			print('Стрелка заблокирована\n')
			return None
		grid[row_idx][col_idx] = '\u00B7'
		print('Стрелка ушла!\n')

	def generate_field(self):
		field = self.create_field()
		directions = []
		for idx_row, row in enumerate(field):
			for idx_col, col in enumerate(row):
				if idx_row < self.SIZE // 2:
					value_1 = self.SYMBOLS['up']
				else:
					value_1 = self.SYMBOLS['down']
				if idx_col < self.SIZE // 2:
					value_2 = self.SYMBOLS['left']
				else:
					value_2 = self.SYMBOLS['right']
				field[idx_row][idx_col] = random.choice([value_1, value_2])
		return field

	def is_empty(self, grid):
		check_grid = list(chain.from_iterable(grid))
		for idx, item in enumerate(list(chain.from_iterable(grid))):
			if item == '\u00B7':
				check_grid[idx] = None
		return not any(check_grid)

	def start(self):
		while True:
			try:
				self.SIZE = int(input('Введите размер игрового поля: '))
			except ValueError:
				print('Введите целое число')
				continue

			if self.SIZE < 1:
				print('Размер поля должен быть больше нуля')
				continue

			break

		grid = self.generate_field()
		while True:
			if self.is_empty(grid):
				print('Игра окончена!')
				break
			else:
				self.draw_field(grid)
				try:
					row, col, direction = input().split()
				except ValueError:
					print('Неверный формат ввода\n')
					continue
				try:
					test_row = int(row)
					test_col = int(col)
				except ValueError:
					print('Неверный формат ввода\n')
					continue
				if direction not in self.DIRECTIONS.keys():
					print('Неизвестное направление\n')
					continue

				self.make_move(grid, row, col, direction)


# Для запуска игры создайте экземпляр игры и вызовите метод start()

game = GameArrows()
game.start()
