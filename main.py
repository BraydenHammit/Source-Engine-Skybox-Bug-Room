import tkinter as tk
from extra_code.movement import move

root = tk.Tk()
root.title('Source Engine Skybox Bug Room')
root.state('zoomed')
root.config(bg='black')
canvas = tk.Canvas(root,bg='grey40',bd=0,highlightbackground="black")
canvas.pack(expand=True,fill='both')
canvas.my, canvas.mx = 0, 0

def ms(event):
    global canvas
    canvas.my = event.y
    canvas.mx = event.x

player = {
    'shape': canvas.create_oval(50,50,-50,-50,fill='red'),
    'color': 'red',
    'stamps': [],
    'size': 50
    }

canvas.bind('<Motion>',ms)
root.after(16,lambda:move(root,player,canvas))
root.mainloop()