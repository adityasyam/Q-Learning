import numpy as np


def getPlayableActions(currentState, differentials, timestep):
    """Returns a list of states reachable from [currentState] after time [timestep]
    has elapsed. [currentState] is a list of 4 numbers: x coordinate, y coordinate, 
    speed, and angle. [differentials] is also 4 numbers, but is the 
    differences between cells in the matrix in SI units. [timestep] is what states are 
    possible after [timestep] amount of time."""
    acceleration_power = 1  # m/s/s
    braking_power = 1  # m/s/s
    max_turning_rate = 30  # deg/s


def getStateMatrix():
    """Returns a tuple, the first element is a matrix with dimensions: x coordinate, 
    y coordinate, speed, angle. The second element is the differences between
    each element of the matrix in SI units. This function should be determined before
    compile-time based on the occupancy grid resolution and other physical factors."""
    return np.zeros((1000, 1000, 10000, 10000, 360))
