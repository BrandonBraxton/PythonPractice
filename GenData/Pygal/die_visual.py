import pygal
from die import Die


die = Die()

#make some rolls and store results in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
#print(results)
## Analyzing results
freq =[]
for value in range(1,die.num_sides+1):
    frequency= results.count(value)
    freq.append(frequency)
    
#print(freq)

#visualize the results

hist = pygal.Bar()

hist.title = "Results of rolling one die 1000 times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6", freq)
hist.render_to_file('die_visual.svg')