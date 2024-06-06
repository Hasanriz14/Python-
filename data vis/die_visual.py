from die_random import Die
import plotly.express as px
die_1 = Die()
die_2 = Die()
result = []
for get_role in range(1000):
    take_res = die_1.roll_dice() * die_2.roll_dice()
    print(take_res)
    result.append(take_res)
max_sides = die_1.die_side + die_2.die_side
frequency = []
poss_result = range(2,max_sides+1)
for value in poss_result :
    frequencies = result.count(value)
    frequency.append(frequencies)
print(f"1: {frequency[0]}\n")
print(f"2: {frequency[1]}\n")
print(f"3: {frequency[2]}\n")
print(f"4: {frequency[3]}\n")
print(f"5: {frequency[4]}\n")
print(f"6: {frequency[5]}\n")
title = "Results of rolling a Die 1000 times"
label = {'x': 'Die-side','y':'frequency'}
fig= px.bar(x = poss_result,y = frequency,title= title, labels= label)
fig.update_layout(xaxis_dtick = 1)
fig.show()
fig.write_html('die_roll_visual.html')