#Cubes: A number raised to the third power is a cube. Plot the first five cubic numbers, and then plot the first 5,000 cubic numbers.
from matplotlib import pyplot as plt
dt = []

for i in range(5000):
    i = i**3
    dt.append(i)
    
print(dt)
plt.style.use('Solarize_Light2')
fig,ax = plt.subplots()

ax.plot(range(len(dt)),dt,linewidth =4)
ax.set_title("Cubes",fontsize =22)
ax.set_xlabel("Value",fontsize = 12)
ax.set_ylabel("Cube value",fontsize = 12)

ax.tick_params(labelsize =14)
ax.ticklabel_format(style = "plain")
plt.show()