# ray_ellipsoid_intersection.py
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
# Determining the intersection point (if any) between a ray and the Earth's reference ellipsoid.

# Parameters:
#  d_l_x: x-component of origin-referenced ray direction
#  d_l_y: y-component of origin-referenced ray direction
#  d_l_z: z-component of origin-referenced ray direction
#  c_l_x: x-component offset of ray origin
#  c_l_y: y-component offset of ray origin
#  c_l_z: z-component offset of ray origin

# Output:
#  l_d[0]: x-component of intersection point
#  l_d[1]: y-component of intersection point
#  l_d[2]: z-component of intersection point

# Written by Thomas Turon
# Other contributors: None
#
# See the LICENSE file for the license.

# import modules
import sys
import math
# constants
R_E_KM = 6378.137 # radius of Earth in km
e_E = 0.081819221456

# initialize script arguments
d_l_x = ''
d_l_y = ''
d_l_z = ''
c_l_x = ''
c_l_y = ''
c_l_z = ''

# script arguments
if len(sys.argv) == 7:
    d_l_x = float(sys.argv[1])
    d_l_y = float(sys.argv[2])
    d_l_z = float(sys.argv[3])
    c_l_x = float(sys.argv[4])
    c_l_y = float(sys.argv[5])
    c_l_z = float(sys.argv[6])

else:
    print(\
   'Usage: '\
   'python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'\
    )
    exit()

# Define each vector for the final output
# l_d vector (initialized with placeholders)
l_d = ['', '', '']

# d_l vector with x, y, and z components
d_l = [d_l_x, d_l_y, d_l_z]

# c_l vector with x, y, and z components
c_l = [c_l_x, c_l_y, c_l_z]

x_sq_component = d_l_x**2
y_sq_component = d_l_y**2
z_sq_component = d_l_z**2
term1 = (z_sq_component / (1 - e_E**2)) + y_sq_component + x_sq_component

x_cross_prod = c_l_x * d_l_x
y_cross_prod = c_l_y * d_l_y
z_cross_prod = c_l_z * d_l_z
term2 = 2*(x_cross_prod + y_cross_prod + (z_cross_prod) / (1 - e_E**2))

x_center_sq = c_l_x**2
y_center_sq = c_l_y**2
z_center_sq = c_l_z**2
term3 = x_center_sq + y_center_sq + (z_center_sq / (1 - e_E**2)) - R_E_KM**2

# Compute the discriminant for the quadratic equation
discriminant = term2**2 - (4.0 * term1 * term3)

# logic for if discriminant is nonnegative
if discriminant >= 0.0:
    d = (-term2 - math.sqrt(discriminant))/(2*term1)
    if d < 0.0:
        d = (-term2 + math.sqrt(discriminant))/(2*term1)
    if d >= 0.0:
        l_d = [d*d_l_x + c_l_x, d*d_l_y + c_l_y, d*d_l_z + c_l_z]
        # print results for existing intersection point
        print(l_d[0]) # x-component of intersection point
        print(l_d[1]) # y-component of intersection point
        print(l_d[2]) # z-component of intersection point