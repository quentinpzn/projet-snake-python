from tkinter import *
from random import randrange

class SnakeGame:
    def __init__(self, root, speed=100, snake_size=20, canvas_width=500, canvas_height=500):
        self.root = root
        self.speed = speed
        self.snake_size = snake_size
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.dx, self.dy = self.snake_size, self.snake_size
        self.direction = 'haut'
        self.flag = 0
        self.paused = True
        self.Serpent = [[245, 245], [245 - self.snake_size, 245], [245 - 2 * self.snake_size, 245]]
        self.pX = self.random_pomme_coord(self.canvas_width)
        self.pY = self.random_pomme_coord(self.canvas_height)
        
        self.can = Canvas(root, width=self.canvas_width, height=self.canvas_height, bg='lightblue')
        self.can.pack(side=TOP, padx=5, pady=5)

        self.pomme = self.can.create_oval(self.pX, self.pY, self.pX + self.snake_size, self.pY + self.snake_size, outline='red', fill='red')

        tex1 = Label(root, text="Appuyez sur 'Espace' pour commencer/pause le jeu.", bg='black', fg='green')
        tex1.pack(padx=0, pady=11)

        root.bind('<Left>', self.left)
        root.bind('<Right>', self.right)
        root.bind('<Up>', self.up)
        root.bind('<Down>', self.down)
        root.bind('<space>', self.toggle_pause)

    def random_pomme_coord(self, max_value):
        return randrange(0, max_value // self.snake_size) * self.snake_size

    def move(self):
        if self.paused:
            return

        self.can.delete('all')
        self.update_snake_position()
        self.draw_snake()
        self.can.create_oval(self.pX, self.pY, self.pX + self.snake_size, self.pY + self.snake_size, outline='red', fill='red')
        self.test()

        if not self.paused:
            self.root.after(self.speed, self.move)

    def update_snake_position(self):
        # Move the snake segments
        for i in range(len(self.Serpent) - 1, 0, -1):
            self.Serpent[i] = list(self.Serpent[i - 1])
        # Update the head position based on the direction
        if self.direction == 'gauche':
            self.Serpent[0][0] -= self.dx
        elif self.direction == 'droite':
            self.Serpent[0][0] += self.dx
        elif self.direction == 'haut':
            self.Serpent[0][1] -= self.dy
        elif self.direction == 'bas':
            self.Serpent[0][1] += self.dy

        # Boundary conditions to wrap around the screen
        if self.Serpent[0][0] < 0:
            self.Serpent[0][0] = self.canvas_width - self.snake_size
        elif self.Serpent[0][0] >= self.canvas_width:
            self.Serpent[0][0] = 0
        if self.Serpent[0][1] < 0:
            self.Serpent[0][1] = self.canvas_height - self.snake_size
        elif self.Serpent[0][1] >= self.canvas_height:
            self.Serpent[0][1] = 0

    def draw_snake(self):
        for i in range(len(self.Serpent)):
            x, y = self.Serpent[i]
            if i == 0:
                # Draw head
                self.draw_head(x, y)
            elif i == len(self.Serpent) - 1:
                # Draw tail
                self.draw_tail(x, y)
            else:
                # Draw body segment
                self.can.create_oval(x, y, x + self.snake_size, y + self.snake_size, outline='brown', fill='lightgreen')

    def draw_head(self, x, y):
        self.can.create_oval(x, y, x + self.snake_size, y + self.snake_size, outline='brown', fill='lightgreen')
        # Draw eyes
        eye_size = self.snake_size // 5
        self.can.create_oval(x + eye_size, y + eye_size, x + 2*eye_size, y + 2*eye_size, outline='black', fill='black')
        self.can.create_oval(x + 3*eye_size, y + eye_size, x + 4*eye_size, y + 2*eye_size, outline='black', fill='black')
        # Draw tongue
        self.can.create_line(x + self.snake_size // 2, y + self.snake_size, x + self.snake_size // 2, y + self.snake_size + 10, fill='red')
        self.can.create_line(x + self.snake_size // 2, y + self.snake_size + 10, x + self.snake_size // 2 - 5, y + self.snake_size + 15, fill='red')
        self.can.create_line(x + self.snake_size // 2, y + self.snake_size + 10, x + self.snake_size // 2 + 5, y + self.snake_size + 15, fill='red')

    def draw_tail(self, x, y):
        self.can.create_oval(x, y, x + self.snake_size, y + self.snake_size, outline='brown', fill='lightgreen')
        # Draw stripes on tail
        stripe_width = self.snake_size // 5
        self.can.create_rectangle(x + stripe_width, y, x + 2 * stripe_width, y + self.snake_size, outline='brown', fill='brown')
        self.can.create_rectangle(x + 3 * stripe_width, y, x + 4 * stripe_width, y + self.snake_size, outline='brown', fill='brown')

    def newGame(self):
        if self.flag == 0:
            self.flag = 1
        self.paused = False
        self.move()

    def toggle_pause(self, event):
        if self.flag == 0:
            self.newGame()
        else:
            self.paused = not self.paused
            if not self.paused:
                self.move()

    def left(self, event):
        if self.direction != 'droite':
            self.direction = 'gauche'

    def right(self, event):
        if self.direction != 'gauche':
            self.direction = 'droite'

    def up(self, event):
        if self.direction != 'bas':
            self.direction = 'haut'

    def down(self, event):
        if self.direction != 'haut':
            self.direction = 'bas'
    
    def test(self):
        head_x, head_y = self.Serpent[0]
        if (head_x < self.pX + self.snake_size and head_x + self.snake_size > self.pX and
            head_y < self.pY + self.snake_size and head_y + self.snake_size > self.pY):
            self.pX = self.random_pomme_coord(self.canvas_width)
            self.pY = self.random_pomme_coord(self.canvas_height)
            self.Serpent.append([self.Serpent[-1][0], self.Serpent[-1][1]])

if __name__ == "__main__":
    fen = Tk()
    game = SnakeGame(fen, speed=100, snake_size=20, canvas_width=600, canvas_height=600)
    fen.mainloop()
