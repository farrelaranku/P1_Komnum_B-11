import matplotlib.pyplot
import numpy

x = numpy.linspace(-10, 10, 750) 

#MASUKKAN FUNGSI DISINI
y = (x*x*x) + (x*x) -(3*x) -3

fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
matplotlib.pyplot.plot(x, y, 'r')
matplotlib.pyplot.show()