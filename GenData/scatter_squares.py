import matplotlib.pyplot as plt

#x_values = [1,2,3,4,5]
#y_values = [1,4,9,16,25]

##calc data automatically
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=40)
#removing outlines from data points
    #plt.scatter(x_values, y_values, edgecolor='none', s=40)
#defining custom colors
    #plt.scatter(x_values, y_values, c = 'red', edgecolor='none', s=40)

#use a colormap
plt.scatter(x_values, y_values, c = y_values, cmap=plt.cm.Reds, edgecolors='None', s=40)

#SAVING PLOTS AUTOMATICALLY
#plt.savefig('squares_plot.png', bbox_inches='tight')


plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize =14)
plt.ylabel("Square of Value", fontsize=14)
#size of tick labels
plt.tick_params(axis='both',which='major', labelsize=14)

#set range for each axis
plt.axis([0, 1100, 0, 1100000])
plt.show()