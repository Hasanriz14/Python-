import matplotlib.pyplot as plt
from randomwalk import RandomWalk
while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    ax.set_aspect('equal')
    
    # Highlight the starting point
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    # Highlight the end point
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    plt.show()
    
    key_input = input("Do you want to continue the loop (Y/N)\n")
    if key_input.lower() == 'n':
        break