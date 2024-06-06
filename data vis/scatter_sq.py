from matplotlib import pyplot as plt
from get_data import Get_data as gd
read_data = gd()
rd_x = read_data.scatter_data_x()
print(rd_x)
rd_y = read_data.scatter_data_y()
print(rd_y)

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(rd_x,rd_y,c=rd_y,cmap=plt.cm.Blues,s = 200)
#set chart title and label axes
ax.set_title('Square plot',fontsize = 24)
ax.set_xlabel('Value',fontsize = 12)
ax.set_ylabel('Square value',fontsize = 12)
# set size of tick labels
ax.tick_params(labelsize =13)
ax.ticklabel_format(style = 'plain')
plt.savefig('plot.png',bbox_inches = 'tight')
