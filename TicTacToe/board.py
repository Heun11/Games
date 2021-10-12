import pygame as p
import pygame.freetype
from random import randint
p.init()

Font = p.freetype.Font("TRASH/tictactoe/assets/font.ttf", 205)
Over_Font = p.freetype.Font("TRASH/tictactoe/assets/font.ttf", 50)

class Board:
    def __init__(self):
        self.board = [
                        [' ',' ',' '],
                        [' ',' ',' '],
                        [' ',' ',' ']
                     ]

        self.click = False
        self.player = randint(1, 2)
        self.winner = 0
        self.over = False
        self.restart = False
        self.total_move = 0
        self.event = None

    def getEvent(self,event):
        self.event = event

    def gameOver(self,i,sur):
        p.draw.rect(sur,((0,0,0)),p.Rect(0,0,600,600))
        if i == 1:
            Over_Font.render_to(sur, (50,100), "Player X won", (255, 255, 255))
        if i == 2:
            Over_Font.render_to(sur, (50,100), "Player O won", (255, 255, 255))
        if i == 0:
            Over_Font.render_to(sur, (50,100), "Tie",(255,255,255))


        # for i in range(3):
        #     for j in range(3):
        #         self.board[j][i] = ' '
        # self.winner = 0
        # self.over = False
        # self.total_move = 0
        # self.restart = False
        

    def check(self):
        for j in range(3):
            if self.board[j][0] == "X" and self.board[j][1] == "X" and self.board[j][2] == "X":
                self.over = True
                self.winner = 1

        for i in range(3):
            if self.board[0][i] == "X" and self.board[1][i] == "X" and self.board[2][i] == "X":
                self.over = True
                self.winner = 1

        for j in range(3):
            if self.board[j][0] == "O" and self.board[j][1] == "O" and self.board[j][2] == "O":
                self.over = True
                self.winner = 2

        for i in range(3):
            if self.board[0][i] == "O" and self.board[1][i] == "O" and self.board[2][i] == "O":
                self.over = True
                self.winner = 2

        if self.total_move == 9:
            self.over = True
            self.winner = 0
        

    def logic(self,i,j):
        mx,my = p.mouse.get_pos()

        for i in range(3):
            for j in range(3):
                if self.click and mx < i*200 + 200 and mx > i*200 and my < j*200 + 200 and my > j*200:
                    if self.board[j][i] == ' ':
                        if self.player == 1:
                            index = "O"
                            self.player = 2

                        elif self.player == 2:
                            index = "X"
                            self.player = 1

                        self.board[j][i] = index
                        self.total_move += 1
        else:
            self.click = False
        

    def update(self):
        if self.event.type == p.MOUSEBUTTONDOWN:
            if self.event.button == 1:
                self.click = True

        if self.event.type == p.KEYDOWN:
            if self.event.key == p.K_w:
                print("click")
                self.restart = True

        self.logic(1, 1)
        self.check()

    def draw(self,sur):

        if self.over == False:
            for y in range(3):
                for x in range(3):
                    p.draw.rect(sur,((0,0,0)),p.Rect(x*205,y*205,195,195))

            for i in range(3):
                for j in range(3):
                    index = self.board[j][i]
                    Font.render_to(sur, (i*205+22,j*205+22), index, (255, 255, 255))

        else:
            self.gameOver(self.winner, sur)
