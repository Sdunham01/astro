import constants as c
import equations as eq
import numpy
import time
import matplotlib.pyplot as pyplot
from matplotlib.patches import Circle

e = 0.5
a = c.r_e * 2.5

itr = 0
ta = 0

radius_vectors = []

while itr < 365:

    r = eq.radiusOrbitEqq(e, a, numpy.deg2rad(ta))

    radius_vector = eq.radisVector(r, numpy.deg2rad(ta))
    radius_vectors.append(radius_vector)

    ta += 1
    itr += 1


x_values = [vec[0] for vec in radius_vectors]
y_values = [vec[1] for vec in radius_vectors]

pyplot.plot(x_values, y_values, '-')

circle_radius = c.r_e
circle = Circle((0, 0), circle_radius, color='green')
pyplot.gca().add_patch(circle)

pyplot.title('Radius Vectors over True Anomaly')
pyplot.xlabel('X Component')
pyplot.ylabel('Y Component')
pyplot.grid(True)
pyplot.show()
