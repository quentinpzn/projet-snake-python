from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk
from random import randrange

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.snake_color = 'light green'
        self.snake_size = 10
        self.bg_image_path = "BGSNAKE.jpg"
        self.bg_image = Image.open(self.bg_image_path)
        self.main_menu()

    def main_menu(self):
        self.clear_widgets()
        
        title = Label(self.root, text="Snake Game", font=('Arial', 24, 'bold'), bg='#4d2600', fg='yellow', relief=GROOVE)
        title.pack(pady=20)

        play_btn = Button(self.root, text="Play", command=self.level_menu, bg='#4d2600', fg='yellow', font=('Arial', 16, 'bold'))
        play_btn.pack(pady=10)

        options_btn = Button(self.root, text="Options", command=self.options_menu, bg='#4d2600', fg='yellow', font=('Arial', 16, 'bold'))
        options_btn.pack(pady=10)

        quit_btn = Button(self.root, text="Quit", command=self.root.destroy, bg='#4d2600', fg='yellow', font=('Arial', 16, 'bold'))
        quit_btn.pack(pady=10)
        
    def level_menu(self):
        self.clear_widgets()
        
        title = Label(self.root, text="Select Difficulty Level", font=('Arial', 18, 'bold'), bg='#4d2600', fg='yellow', relief=GROOVE)
        title.pack(pady=20)
        
        easy_btn = Button(self.root, text="Easy", command=lambda: self.start_game(speed=40), bg='#4d2600', fg='yellow', font=('Arial', 16, 'bold'))
        easy_btn.pack(pady=10)
        
        medium_btn = Button(self.root, text="Medium", command=lambda: self.start_game(speed=20), bg='#4d2600', fg='yellow', font=('Arial', 16, 'bold'))
        medium_btn.pack(pady=10)
        
        hard_btn = Button(self.root, text="Hard", command=lambda: self.start_game(speed=10), bg='#4d2600', fg='yellow', font=('Arial', 16, 'bold'))
        hard_btn.pack(pady=10)
        
        back_btn = Button(self.root, text="Back", command=self.main_menu, bg='#4d2600', fg='yellow', font=('Arial', 16, 'bold'))
        back_btn.pack(pady=10)

    def options_menu(self):
        self.clear_widgets()
        
        title = Label(self.root, text="Options", font=('Arial', 18, 'bold'), bg='#4d2600', fg='yellow', relief=GROOVE)
        title.pack(pady=20)
        
        snake_color_btn = Button(self.root, text="Snake Color", command=self.choose_snake_color, bg='#4d2600', fg='yellow', font=('Arial', 16, 'bold'))
        snake_color_btn.pack(pady=10)
        
        back_btn = Button(self.root, text="Back", command=self.save_options, bg='#4d2600', fg='yellow', font=('Arial', 16, 'bold'))
        back_btn.pack(pady=10)
    
    def choose_snake_color(self):
        color = askcolor()[1]
        if color:
            self.snake_color = color
    
    def save_options(self):
        self.main_menu()
    
    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def start_game(self, speed):
        self.clear_widgets()
        self.canvas = Canvas(self.root, width=500, height=500)
        self.canvas.pack(side=TOP, padx=5, pady=5)
        self.root.update_idletasks()

        self.speed = speed
        self.dx = self.dy = self.snake_size
        self.direction = 'haut'
        self.flag = 0
        self.paused = False
        self.score = 0
        self.Serpent = [[245, 245], [245 + self.snake_size, 245], [245 + 2 * self.snake_size, 245]]
        self.update_apple_position()
        
        self.score_label = Label(self.root, text="Score: 0", font=('Arial', 14, 'bold'), bg='#4d2600', fg='yellow')
        self.score_label.pack()

        back_btn = Button(self.root, text="Back to Menu", command=self.back_to_menu, bg='#4d2600', fg='yellow', font=('Arial', 16, 'bold'))
        back_btn.pack(pady=10)

        self.root.bind('<Right>', self.right)
        self.root.bind('<Left>', self.left)
        self.root.bind('<Up>', self.up)
        self.root.bind('<Down>', self.down)
        self.root.bind('<space>', self.toggle_pause)

        self.start_game_loop()

    def draw(self):
        self.canvas.delete('all')
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image.resize((self.canvas.winfo_width(), self.canvas.winfo_height())))
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg_image_tk)
            
        for segment in self.Serpent:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + self.snake_size, y + self.snake_size, outline='green', fill=self.snake_color)
        self.canvas.create_oval(self.pX, self.pY, self.pX + self.snake_size, self.pY + self.snake_size, outline='red', fill='red')
    
    def update(self):
        if self.paused:
            return

        # Move the snake
        for i in range(len(self.Serpent) - 1, 0, -1):
            self.Serpent[i] = list(self.Serpent[i - 1])
        if self.direction == 'gauche':
            self.Serpent[0][0] -= self.dx
        elif self.direction == 'droite':
            self.Serpent[0][0] += self.dx
        elif self.direction == 'haut':
            self.Serpent[0][1] -= self.dy
        elif self.direction == 'bas':
            self.Serpent[0][1] += self.dy

        # Check for collisions with the wall
        if self.Serpent[0][0] < 0:
            self.Serpent[0][0] = self.canvas.winfo_width() - self.snake_size
        elif self.Serpent[0][0] >= self.canvas.winfo_width():
            self.Serpent[0][0] = 0
        if self.Serpent[0][1] < 0:
            self.Serpent[0][1] = self.canvas.winfo_height() - self.snake_size
        elif self.Serpent[0][1] >= self.canvas.winfo_height():
            self.Serpent[0][1] = 0

        # Check for collisions with the apple
        head_x, head_y = self.Serpent[0]
        if (head_x < self.pX + self.snake_size and head_x + self.snake_size > self.pX and
            head_y < self.pY + self.snake_size and head_y + self.snake_size > self.pY):
            self.update_apple_position()
            self.Serpent.append([self.Serpent[-1][0], self.Serpent[-1][1]])
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")

        # Check for collisions with itself
        for segment in self.Serpent[1:]:
            if segment == self.Serpent[0]:
                self.game_over()
                return

    def update_apple_position(self):
        max_width = self.canvas.winfo_width()
        max_height = self.canvas.winfo_height()
        self.pX = self.random_coord(max_width)
        self.pY = self.random_coord(max_height)

    def random_coord(self, max_value):
        return randrange(1, max_value // self.snake_size) * self.snake_size

    def move(self):
        if self.paused:
            return
        self.update()
        self.draw()
        if self.flag != 0:
            self.canvas.after(self.speed, self.move)

    def start_game_loop(self):
        if self.flag == 0:
            self.flag = 1
        self.paused = False
        self.move()

    def toggle_pause(self, event=None):
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

    def back_to_menu(self):
        self.clear_widgets()
        self.main_menu()

    def game_over(self):
        self.clear_widgets()
        
        game_over_label = Label(self.root, text="GAME OVER", font=('Arial', 24, 'bold'), bg='#4d2600', fg='red', relief=GROOVE)
        game_over_label.pack(pady=20)

        score_label = Label(self.root, text=f"Final Score: {self.score}", font=('Arial', 18, 'bold'), bg='#4d2600', fg='yellow')
        score_label.pack(pady=10)

        replay_btn = Button(self.root, text="Replay", command=self.level_menu, bg='#4d2600', fg='yellow', font=('Arial', 16, 'bold'))
        replay_btn.pack(pady=10)

        quit_btn = Button(self.root, text="Quit", command=self.root.destroy, bg='#4d2600', fg='yellow', font=('Arial', 16, 'bold'))
        quit_btn.pack(pady=10)

if __name__ == "__main__":
    fen = Tk()
    game = SnakeGame(fen)
    fen.mainloop()
