from math import pi
from math import cos
from math import tan
#imported necessary mathematical modules

#Converting degrees to radians with the above
# y = height of projectile
# y = height of barrel + tan(thetha elevation angle in radians) - 9.81*(horizontal distance)squared/2(initial velocity*cos*theta elevation in radians)squared
g = 9.81
v0 =  44
theta = 80 * (pi/180)
x = 0.5
y0 = 1
#listing all the variables I will need

y = (y0 + x*tan(theta)) - (g*x**2)/(2*(v0*cos(theta))**2)
#calculation as per the formula
print(y)
