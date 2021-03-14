from objects import Window
from settings import HEIGHT, WIDTH


root = Window()
root.iconbitmap('static\\Group3.ico')
root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('XO game')
root.set_main_menu()

root.mainloop()
