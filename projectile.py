from math import pi
from math import cos
from math import tan
# #imported necessary mathematical modules
#
# #Converting degrees to radians with the above
# # y = height of projectile
# # y = height of barrel + tan(thetha elevation angle in radians) - 9.81*(horizontal distance)squared/2(initial velocity*cos*theta elevation in radians)squared
# g = 9.81
# v0 =  44
# theta = 80 * (pi/180)
# x = 0.5
# y0 = 1
# #listing all the variables I will need
#
# y = (y0 + x*tan(theta)) - (g*x**2)/(2*(v0*cos(theta))**2)
# #calculation as per the formula
# print(y)

# milena's code
from math import pi, tan, cos
bh = 1
x = 0.5
theta_degrees = 80
velocity = 44
g = 9.81
theta_radians = theta_degrees*(pi/180)
y = bh + x*tan(theta_radians) - (g * pow(x, 2))/(2*pow(velocity*cos(theta_radians), 2))
print(y)