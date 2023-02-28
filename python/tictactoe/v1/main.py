import traceback

class TicTacToe:
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.current_player = 'X'
        self.game_won = False
        self.start_game()

    def draw(self):
        for row in self.board:
            print(row)

    def get_input(self):
        coord = input('PLAYER {}: ENTER COORDINATE(x,y): '.format(self.current_player))
        coord = coord.split(',')
        if len(coord) != 2:
            print('IMPROPER FORMAT: FORMAT MUST BE (x,y) ')
            self.get_input()
        try:
            coord[0] = int(coord[0])
            coord[1] = int(coord[1])
        except ValueError:
            self.get_input()
        print('COORD: {}'.format(coord))
        if coord[0] > 2 or coord[0] < 0 or coord[1] > 2 or coord[1] < 0:
            print('NOT A SUITABLE COORD')
            self.get_input()
        board_coord = self.board[coord[0]][coord[1]]

        if board_coord != ' ':
            print('POSITION ALREADY OCCUPIED')
            self.get_input()
        else:
            self.board[coord[0]][coord[1]] = self.current_player
            self.check_for_winner()
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'

    def start_game(self):
        while not self.game_won:
            self.draw()
            self.get_input()

    def check_for_winner(self):
        for i in range(0, 3):
            col_str = ''
            for j in range(0, 3):
                col_str += self.board[i][j]

            if col_str == 'XXX' or col_str == 'OOO':
                self.game_won = True
                print('GAME WON BY PLAYER: {}'.format(self.current_player))
                self.draw()
                return

        for row in self.board:
            row_str = ''.join(row)
            print(row_str)
            if row_str == 'XXX' or row_str == 'OOO':
                self.game_won = True
                print('GAME WON BY PLAYER: {}'.format(self.current_player))
                self.draw()
                return

        diag_l = ''.join([self.board[0][0], self.board[1][1], self.board[2][2]])
        diag_r = ''.join([self.board[0][2], self.board[1][1], self.board[2][0]])
        print('diag l: {}\ndiag r: {}\n'.format(diag_l, diag_r))
        if diag_l == 'XXX' or diag_l == 'XXX' or diag_r == 'XXX' or diag_r == 'OOO':
            self.game_won = True
            print('GAME WON BY PLAYER: {}'.format(self.current_player))
            self.draw()
            return

if __name__ == '__main__':
    print('hello world')
    game = TicTacToe()
