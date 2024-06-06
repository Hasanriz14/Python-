import matplotlib.pyplot as plt
from get_data import Get_data as gd
sq = gd()
data  = sq.send_data()
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
print(data)
print("Press 'q' to exit\n")
if not data:
    print("No data to plot.")
else:

    ax.plot(range(len(data)),data, linewidth =3)
    # Set chart title and label axes
    ax.set_title("square Numbers",fontsize =  22)
    ax.set_xlabel("Value",fontsize= 12)
    ax.set_ylabel("square of value",fontsize = 14)

    #set size of tick labels
    ax.tick_params(labelsize = 13)
    plt.show()
get_input = input("Press 'q' to exit")
if get_input == 'q':
    exit
    