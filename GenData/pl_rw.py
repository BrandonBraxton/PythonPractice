import matplotlib.pyplot as plt
from random_walk import RandomWalk

#make random walk
#generate multiple randwalk
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    #alter size to fill screen
    
    plt.figure(dpi=128, figsize=(10,6))
    plt.scatter(rw.x_values, rw.y_values,c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    
    plt.show()
    
    keepRunning = input("Make Another Walk?(y/n)")
    if keepRunning == 'n':
        break