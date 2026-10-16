colors = [
    '#FF0000', '#FF0F00', '#FF1E00', '#FF2D00', '#FF3D00', '#FF4C00', '#FF5B00', '#FF6B00', '#FF7A00', '#FF8900', 
    '#FF9900', '#FFA800', '#FFB700', '#FFC600', '#FFD600', '#FFE500', '#FFF400', '#F9FF00', '#EAFF00', '#DBFF00', 
    '#CBFF00', '#BCFF00', '#ADFF00', '#9EFF00', '#8EFF00', '#7FFF00', '#70FF00', '#60FF00', '#51FF00', '#42FF00', 
    '#33FF00', '#23FF00', '#14FF00', '#05FF00', '#00FF0A', '#00FF19', '#00FF28', '#00FF38', '#00FF47', '#00FF56', 
    '#00FF66', '#00FF75', '#00FF84', '#00FF93', '#00FFA3', '#00FFB2', '#00FFC1', '#00FFD1', '#00FFE0', '#00FFEF', 
    '#00FFFF', '#00EFFF', '#00E0FF', '#00D1FF', '#00C1FF', '#00B2FF', '#00A3FF', '#0093FF', '#0084FF', '#0075FF', 
    '#0066FF', '#0056FF', '#0047FF', '#0038FF', '#0028FF', '#0019FF', '#000AFF', '#0500FF', '#1400FF', '#2300FF', 
    '#3200FF', '#4200FF', '#5100FF', '#6000FF', '#7000FF', '#7F00FF', '#8E00FF', '#9E00FF', '#AD00FF', '#BC00FF', 
    '#CC00FF', '#DB00FF', '#EA00FF', '#F900FF', '#FF00F4', '#FF00E5', '#FF00D6', '#FF00C6', '#FF00B7', '#FF00A8', 
    '#FF0098', '#FF0089', '#FF007A', '#FF006B', '#FF005B', '#FF004C', '#FF003D', '#FF002D', '#FF001E', '#FF000F'
]

def move(root,player,canvas):
    x = canvas.mx
    y = canvas.my
    s = player['size']

    if player['follow']:
        canvas.coords(player['shape'], x-s, y-s, x+s, y+s)
        cds = canvas.coords(player['shape'])
        player['stamps'].append(canvas.create_oval(cds[0],cds[1],cds[2],cds[3],fill=player['color']))

    if player['dis']:
        player['disNUM'] += 1
        try:
            player['color'] = colors[player['disNUM']]
        except IndexError:
            player['disNUM'] = 0
            player['color'] = colors[player['disNUM']]
        canvas.itemconfig(player['shape'],fill=player['color'])

    root.after(16,lambda:move(root,player,canvas))