import matplotlib.pyplot as plot
# set up your lists
numlist = [8, 6, 5, 3]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
colorlist = ['red', 'green', 'purple', 'yellow' ]
explodelist = [0.1, 0.2, 0.3, 0.4]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.2f%%', colors=colorlist,
    	explode = explodelist, startangle = 60)
plot.axis('equal')
plot.savefig('piechart.png')
