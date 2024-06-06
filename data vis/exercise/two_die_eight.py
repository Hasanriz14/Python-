from die_random import Die
import plotly.express as px
die_1 = Die(8)
die_2 = Die(8)
result  = []
for i in range(1000):
    take_val = die_1.roll_dice() + die_2.roll_dice()
    result.append(take_val)

max_sides = die_1.die_side + die_2.die_side
frequency = []
poss_result = range(2,max_sides + 1)
for val in poss_result:
    frequencies = result.count(val)
    frequency.append(frequencies) 

title = "Roliing a dice a 1000 times with die 8"
label = {'x':'Die','y':'frequency'}
fig = px.bar(x = poss_result,y = frequency,title= title,labels= label)
fig.update_layout(xaxis_dtick = 1)
fig.show()