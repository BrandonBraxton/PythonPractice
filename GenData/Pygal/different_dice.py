import pygal
from die import Die


die_1 = Die()
die_2 = Die(10)

#make some rolls and store results in a list
results = []
for roll_num in range(50000):
    result = die_1.roll()+die_2.roll()
    results.append(result)
    
#print(results)
## Analyzing results
freq =[]
max = die_1.num_sides + die_2.num_sides
for value in range(2,max+1):
    frequency= results.count(value)
    freq.append(frequency)
    
#print(freq)

#visualize the results

hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50000 times"
for i in range(2,max+1):
    hist.x_labels = str(i)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D10", freq)
hist.render_to_file('diff_dice_visual.svg')