from die_random import Die
import plotly.express as px
die_A = Die()
die_B = Die()
die_C = Die()
result = []
for i in range(5000):
    get_val = die_A.roll_dice() + die_B.roll_dice() + die_C.roll_dice()
    result.append(get_val)

max_sides = die_A.die_side + die_B.die_side + die_C.die_side
frequency = []

poss_result = range(3,max_sides + 1)


for i in poss_result :
    frequencies = result.count(i)
    frequency.append(frequencies)

for index,res in enumerate(frequency):
    print(f"{index+1}: {res}")
title = 'Three dice counted to 1000 times'
label = {'x' : 'Dice values','y': 'Frequency'}
fig = px.bar(x= poss_result,y = frequency,title= title,labels= label)
fig.update_layout(xaxis_dtick =1)
# fig.show()