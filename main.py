import os

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 9

def draw_board():
	print('_'*13)
	print(f'| {lst[0]} | {lst[1]} | {lst[2]} |')
	print('_'*13)
	print(f'| {lst[3]} | {lst[4]} | {lst[5]} |')
	print('_'*13)
	print(f'| {lst[6]} | {lst[7]} | {lst[8]} |')
	print('_'*13)
	
def x_turn():
	x = int(input('Ходит КРЕСТИК: '))-1
	lst[x] = 'x'
	
def o_turn():
	o = int(input('Ходит НОЛИК: '))-1
	lst[o] = 'o'
	
def check_win():
	if lst[0] == lst[1] and lst[0] == lst[2]:
		return who_win(lst[0])
	elif lst[3] == lst[4] and lst[3] == lst[5]:
		return who_win(lst[3])
	elif lst[6] == lst[7] and lst[6] == lst[8]:
		return who_win(lst[6])
	elif lst[0] == lst[3] and lst[0] == lst[6]:
		return who_win(lst[0])
	elif lst[1] == lst[4] and lst[1] == lst[7]:
		return who_win(lst[1])
	elif lst[2] == lst[5] and lst[2] == lst[8]:
		return who_win(lst[2])
	elif lst[0] == lst[4] and lst[0] == lst[8]:
		return who_win(lst[0])
	elif lst[2] == lst[4] and lst[2] == lst[6]:
		return who_win(lst[2])
		
def who_win(sign):
	if sign == 'x':
		return 'Выиграл КРЕСТИК'
	return 'Выиграл НОЛИК'
	
if __name__=='__main__':
	
	while True:
		os.system('clear')
		draw_board()
		x_turn()
		os.system('clear')
		draw_board()
		counter -= 1
		if check_win():
			print(check_win())
			break
		o_turn()
		os.system('clear')
		draw_board()
		counter -=1
		if check_win():
			print(check_win)
			break
		if not counter:
			print('НИЧЬЯ')
			break
