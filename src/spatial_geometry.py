


# Various routines for vector geometry, rotations, etc.
# References:
# [1] John J. Craig, Introduction to Robotics, 3rd ed., 2005. 

from math import sin,  cos
import numpy as N

def general_axis_rotation(axis,  angle):
    """Generates a rotation matrix around <axis> by <angle>, using the right-hand
    rule.
    Arguments: 
        axis - a 3-component 1D array representing a unit vector
        angle - rotation counterclockwise in radians around the axis when the axis 
            points to the viewer.
    Returns: A 3x3 array representing the matrix of rotation.
    Reference: [1] p.47
    """
    s = sin(angle); c = cos(angle); v = 1 - c
    add = N.array([[0,          -axis[2], axis[1]],  
                            [axis[2],  0,          -axis[0]], 
                            [-axis[1], axis[0],  0        ] ])
    return N.multiply.outer(axis,  axis)*v + N.eye(3)*c + add*s

def generate_transform(axis, angle, translation):
    """Generates a transformation matrix                                                      
    Arguments: axis - a 1D array giving the unit vector to rotate about                       
    angle - angle of rotation about the given axis in the parent frame                         
    translation - a 2D column vector giving the translation along the parent frame           
    """
    rot = general_axis_rotation(axis, angle)
    return N.vstack((N.hstack((rot, translation)), N.r_[[0,0,0,1]]))
