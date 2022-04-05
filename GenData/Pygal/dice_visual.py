import pygal
from die import Die


die_1 = Die()
die_2 = Die()

#make some rolls and store results in a list
results = []
for roll_num in range(1000):
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

hist.title = "Results of rolling two dice 1000 times"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D6", freq)
hist.render_to_file('dice_visual.svg')