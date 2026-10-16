import tkinter as tk
from extra_code.movement import move

root = tk.Tk()
root.title('Source Engine Skybox Bug Room')
try: root.state('zoomed')
except: None
root.config(bg='black')
canvas = tk.Canvas(root,bg='grey40',bd=0,highlightbackground="black")
canvas.pack(expand=True,fill='both')
canvas.my, canvas.mx = 0, 0

def ms(event):
    global canvas
    canvas.my = event.y
    canvas.mx = event.x

def plus_size(_):
    global player
    if player['size'] >= 0:
        player['size']-=5
    else:
        player['size']+=5

def minus_size(_):
    global player
    if player['size'] >= 0:
        player['size']+=5
    else:
        player['size']-=5

def follow_alternate(_):
    global player
    if player['follow']:
        player['follow'] = False
    else:
        player['follow'] = True

def disco(_):
    global player
    if player['dis']:
        player['dis'] = False
    else:
        player['dis'] = True

player = {
    'shape': canvas.create_oval(50,50,-50,-50,fill='#FF0000'),
    'color': '#FF0000',
    'stamps': [],
    'size': 50,
    'follow': True,
    'disNUM': 0,
    'dis': False
    }

canvas.bind('<Motion>',ms)
root.bind('<Up>',minus_size)
root.bind('<Down>',plus_size)
root.bind('<space>',follow_alternate)
root.bind('<q>',disco)
root.after(1,lambda:move(root,player,canvas))
root.mainloop()