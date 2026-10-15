def move(root,player,canvas):
    x = canvas.mx
    y = canvas.my
    s = player['size']

    canvas.coords(player['shape'], x-s, y-s, x+s, y+s)
    cds = canvas.coords(player['shape'])
    player['stamps'].append(canvas.create_oval(cds[0],cds[1],cds[2],cds[3],player['color']))

    root.after(16,lambda:move(root,player,canvas))