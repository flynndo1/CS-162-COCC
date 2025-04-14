import matplotlib.pyplot as plot

# set up your lists
numlist = [13, 10, 2, 5]
namelist = ['Elves', 'Leprechauns', 'Goblins', 'Banshees']
colorlist = ['springgreen', 'darkmagenta', 'burlywood', 'firebrick' ]
explodelist = [0.1, 0.1, 0.1, 0.1]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.0f%%', colors=colorlist,
    	explode = explodelist, startangle = 20)
plot.axis('equal')
plot.savefig('piechart.png')
plot.show()