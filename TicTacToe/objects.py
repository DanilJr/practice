from tkinter import Tk, Label, Button, Entry, ttk, font, Text, StringVar
from settings import BUT_WIDTH, BUT_HEIGHT, HEIGHT, WIDTH#, QUEUE
from functions import check_win
from collections import deque
from PIL import Image, ImageTk
from datetime import datetime


class Picture:
    def __init__(self, path):
        self.img = ImageTk.PhotoImage(Image.open(path))


class But(Button):
    def __init__(self, canvas=None, text=None, font=None, width=None,
                 height=None, command=None, grid=None, img=None):
        self.but = Button(canvas)
        self.but['font'] = font
        self.but['text'] = text            # DANIL!!!!!!!!!!!!!!!
        self.but['width'] = width          # Ask abouot this implementation!!!!
        self.but['height'] = height        # Look below!!!!!!!!!!!!
        self.but['command'] = command
        self.but['image'] = img
        if not grid:
            self.but.pack()
        else:
            self.but.grid(row=grid[0], column=grid[1])

    def set_img(self):
        pass


class Window(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_main_menu(self):
        frame = ttk.Frame(self, padding=12, borderwidth=5, relief="ridge")
        frame.pack()
        But(frame, text='Go game', width=BUT_WIDTH, height=BUT_HEIGHT,
            command=self.set_sides)
        But(frame, text='Logs', width=BUT_WIDTH, height=BUT_HEIGHT,
            command=Log.get_logs)
        But(frame, text='Exit', width=BUT_WIDTH, height=BUT_HEIGHT,
            command=self.destroy)

    def set_sides(self):
        self.destroy()
        new_field = Window()
        new_field.geometry(f'{WIDTH}x{HEIGHT}')
        nameX = StringVar()
        nameO = StringVar()
        Label(new_field, text='Enter player(X) name').pack()
        p1 = Entry(new_field, width=100, textvariable = nameX, font='Arial 14')
        p1.pack()
        Label(new_field, text='Enter player(O) name').pack()
        p2 = Entry(new_field, width=100, textvariable = nameO, font='Arial 14')
        p2.pack()
        QUEUE = deque()
        QUEUE.append(Player(nameX, 'X', 'static\\X.jpg', 0))
        QUEUE.append(Player(nameO, 'O', 'static\\o.jpg', 0))
        But(new_field, text='start game', width=BUT_WIDTH, height=BUT_HEIGHT,
            command=lambda QUEUE=QUEUE:[Window.game_field(QUEUE), new_field.destroy(),
                                        QUEUE[0].set_name(), QUEUE[1].set_name()])

    @classmethod
    def game_field(cls, QUEUE):
        map = [['#', '#', '#'],
               ['#', '#', '#'],
               ['#', '#', '#']]
        game_field = Window()
        game_field.geometry(f'{WIDTH}x{HEIGHT}')
        frame = ttk.Frame(game_field, padding=12, borderwidth=5, relief="ridge")
        frame.pack()
        button_font = font.Font(family='Helvitica', size='50')
        for row in range(3):
            for col in range(3):
                map[row][col] = But(frame, text='#', width=20, font=button_font,
                                    height=10, command=lambda field=game_field,
                                    map=map, row=row, col=col:
                                    QUEUE[0].push_button(game_field, map, row, col, QUEUE),
                                    grid=(row, col))#.but['text']

    def exit(self, QUEUE, log):
        log.set_log(f'{datetime.now()}\n{QUEUE[0]}\n{QUEUE[1]}\n')
        self.set_main_menu()
        self.destroy()


class Player:
    moves = 0

    def __init__(self, name, label, img, win_counter):
        self.name = name
        self.label = label
        self.img = Picture(img)
        self.win_counter = win_counter

    def set_name(self):
        self.name = self.name.get()

    def push_button(self, field, map, row, col, QUEUE):
        print(f'{self.name}- moves')
        if map[row][col].but['text'] in {QUEUE[0].label, QUEUE[1].label}:
            print('sorry need to choose another position\n'*5)
            return None
        map[row][col].but['text'] = self.label
        QUEUE.rotate(1)
        Player.moves += 1
        if check_win(map):
            self.win_counter += 1
            self.set_result(QUEUE, field)
            return None
        if Player.moves == 8:
            self.set_result(QUEUE, field)

    def set_result(self, QUEUE, field):
        Player.moves = 0
        if QUEUE[0].label != 'X':
            QUEUE.rotate(1)
        log = Log()
        field.destroy()
        after_game_menu = Window()
        But(after_game_menu, text='Again?', width=30, height=10,
            command=lambda QUEUE=QUEUE: [Window.game_field(QUEUE),
                                         after_game_menu.destroy()])
        But(after_game_menu, text='Exit', width=30, height=10,
            command=lambda QUEUE=QUEUE, log=log: after_game_menu.exit(QUEUE, log))

    def __str__(self):
        return f'{self.name} while playing {self.label} have won {self.win_counter} times!!!'


class Log:
    def __init__(self):
        self.text = None

    def set_log(self, text):
        self.text = text
        with open('logs.txt', 'a') as f:
            f.write(self.text)

    @classmethod
    def get_logs(cls):
        logs = Text(Window())
        with open('logs.txt', 'r') as f:
            logs.insert(1.0, f.read())
            logs.pack()
