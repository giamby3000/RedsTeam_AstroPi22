import matplotlib.pyplot as plt
from matplotlib import pyplot
import csv
from matplotlib import pylab

x = []
y = []

fig = plt.figure()
#fig = pylab.gcf()
fig.canvas.set_window_title('Astropi RedsTeam Elevation Plot')

plt.rcParams.update({
    "figure.facecolor":  (1.0, 1.0, 1.0, 0.5),  # red   with alpha = 30%
    "axes.facecolor":    (1.0, 1.0, 1.0, 0.5),  # green with alpha = 50%
    "savefig.facecolor": (0.0, 0.0, 1.0, 0.2),  # blue  with alpha = 20%
    "figure.figsize": (60,50),
})



# Initialise the subplot function using number of rows and columns
plot1 = plt.subplot2grid((1, 1), (0, 0), colspan=2)


with open('HeaderLog1.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines:
		x.append(row[0])
		y.append(((row[7])))
#plot1.scatter(x,y)
plot1.plot(x, y, color = 'r', marker = 'o',markersize=1, markeredgecolor="red",label = "PIR activation")


plot1.legend(loc='lower left')
plot1.set_title('Motion detection activations')
plot1.set_ylabel('')
plot1.grid(True)
plot1.get_xaxis().set_visible(False)



plt.ylim(-0.2,2.0)

plt.xlabel("Time")

fig.suptitle('ASTROPI REDSTEAM ISS MOTION DETECTION ANALYSIS', fontsize=30, color='r')

plt.show()