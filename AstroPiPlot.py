import matplotlib.pyplot as plt
from matplotlib import pyplot
import csv
from matplotlib import pylab

x = []
y = []
z = []
k = []
j = []
u = []

fig = plt.figure()
#fig = pylab.gcf()
fig.canvas.set_window_title('Astropi RedsTeam Data Analisys')

plt.rcParams.update({
    "figure.facecolor":  (1.0, 1.0, 1.0, 0.5),  # red   with alpha = 30%
    "axes.facecolor":    (1.0, 1.0, 1.0, 0.5),  # green with alpha = 50%
    "savefig.facecolor": (0.0, 0.0, 1.0, 0.2),  # blue  with alpha = 20%
    "figure.figsize": (50,30),
})


#fig.patch.set_facecolor('white')
#fig.patch.set_alpha(0.6)
#ax = fig.add_subplot(111)
#ax.patch.set_facecolor('white')
#ax.patch.set_alpha(1.0)

# Initialise the subplot function using number of rows and columns
plot1 = plt.subplot2grid((4, 2), (0, 0), colspan=2)
plot2 = plt.subplot2grid((4, 2), (1, 0), colspan=2)
plot3 = plt.subplot2grid((4, 2), (2, 0), colspan=2)
plot4 = plt.subplot2grid((4, 2), (3, 0), colspan=2)

with open('/home/rgb/Documenti/RedsTeamDataLogSamples.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines:
		x.append(row[0])
		y.append((float(row[4])))
		k.append((float(row[1])))		
		j.append((float(row[2])))
		u.append((float(row[3])))



plot1.plot(x, y, color = 'r', linestyle = 'solid', marker = '',label = "g value")


plot1.legend(loc='lower left')
#plot1.set_xticklabels(x, rotation=90, ha='right')
plot1.set_title('Gravitational acceleration Log')
plot1.set_ylabel('g value (m/s2)')
#plot1.set_xlabel('Time')
#plot1.patch.set_facecolor('white')
plot1.grid(True)
plot1.get_xaxis().set_visible(False)

plot2.plot(x, k, color = 'b', linestyle = 'solid', marker = '',label = "x axis acceleration")
plot2.legend(loc='lower left')
plot2.set_title('x axis g acceleration ')
plot2.set_ylabel('g component x')
#plot2.set_xlabel('Time')
#plot2.patch.set_facecolor('white')
#plot2.set_xticklabels(x, rotation=90, ha='right')
plt.gca().axes.get_xaxis().set_visible(False)
plot2.grid(True)
plot2.get_xaxis().set_visible(False)

plot3.plot(x, j, color = 'g', linestyle = 'solid', marker = '',label = "y axis acceleration")
plot3.legend(loc='lower left')
plot3.set_title('y axis g acceleration ')
plot3.set_ylabel('g component y')
#plot3.set_xlabel('Time')
#plot3.patch.set_facecolor('white')
#plot3.set_xticklabels(x, rotation=90, ha='right')
plot3.grid(True)
plot3.get_xaxis().set_visible(False)


plot4.plot(x, u, color = 'orange', linestyle = 'solid', marker = '',label = "z axis acceleration")
plot4.legend(loc='lower left')
plot4.set_title('z axis g acceleration ')
plot4.set_ylabel('g component z')
#plot4.set_xlabel('Time')
#plot4.patch.set_facecolor('white')
#plot4.set_xticklabels(x, rotation=90, ha='right')
plot4.grid(True)

plt.ylim(-0.2,0.15)
#plt.xticks(rotation = 90)
plot4.get_xaxis().set_visible(False)
plt.xlabel("Time")
#mng = plt.get_current_fig_manager()
#plt.get_current_fig_manager().window.state('normal')





#mng.window.showMaximized()
#mng.resize(*mng.window.maxsize())
# mng.full_screen_toggle()
#plt.annotate('subplot ' + str(ax), xy = (1, 0.5), va = 'center', ha = 'center')
#plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

#plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
fig.suptitle('ASTROPI REDSTEAM ANALISYS', fontsize=30, color='r')

plt.show()
