import random
import time
from tkinter import *


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 230, 130)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = FALSE
        self.canvas.bind_all('<Button-1>', self.start)
        self.game_point = 0

    def draw(self):
        if self.paddle.game_state == 0:
            self.canvas.move(self.id, self.x, self.y)
            pos = self.canvas.coords(self.id)
            if self.hit_paddle(pos) == TRUE:
                self.y = -3
            if pos[0] <= 0:
                self.x = 3
            if pos[1] <= 0:
                self.y = 3
            if pos[2] >= self.canvas_width:
                self.x = -3
            if pos[3] >= self.canvas_height:
                self.hit_bottom = TRUE
                self.canvas.itemconfig(end_text, state='normal')
                self.paddle.game_state = 1

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.get_point()
                return TRUE
        return FALSE

    def start(self, evt):
        if self.paddle.game_state == 0:
            self.hit_bottom = FALSE
            self.canvas.itemconfig(start_text, state='hidden')
        if self.paddle.game_state == 1:
            self.restate()

    def get_point(self):
        self.game_point = self.game_point + 1
        self.canvas.itemconfig(game_point_text, text=str(self.game_point) + ' 分')

    def restate(self):
        # self.canvas.move(self.id, 230, 130)
        # self.canvas.move(self.paddle.id, 200, 300)
        self.canvas.itemconfig(end_text, state='hidden')
        self.canvas.itemconfig(start_text, state='normal')
        self.hit_bottom = TRUE
        self.paddle.game_state = 0
        self.game_point = 0


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-a>', self.turn_left)
        self.canvas.bind_all('<KeyPress-d>', self.turn_right)
        # 0-开始游戏；1-重开游戏
        self.game_state = 0

    def turn_left(self, evt):
        if self.game_state == 0:
            self.x = -2

    def turn_right(self, evt):
        if self.game_state == 0:
            self.x = 2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0


tk = Tk()
tk.title("欢乐弹弹球")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
start_text = canvas.create_text(245, 150, text='点击鼠标左键\n\r  开始游戏', font=('黑体', 25), fill='green')
end_text = canvas.create_text(245, 150, text='游 戏 结 束', font=('黑体', 25), fill='red', state='hidden')
game_point_text = canvas.create_text(40, 20, text='0 分', font=('黑体', 11), fill='black')
canvas.pack()
canvas.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
ball.hit_bottom = TRUE

while 1:
    if ball.hit_bottom == FALSE:
        paddle.draw()
        ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
