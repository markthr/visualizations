import numpy as np

MPH_TO_MPS = 0.44704
MPS_TO_MPH = 2.23694
DEG_TO_RAD = np.pi / 180
RAD_TO_DEG = 180 / np.pi
M_TO_FT = 3.28084
DT = 0.001

# Model 1: No Drag
def distance_no_drag(g, launch_angle = 27.5, exit_velocity = 100):

    v_x = MPH_TO_MPS * exit_velocity * np.cos(launch_angle * DEG_TO_RAD)
    v_y = MPH_TO_MPS * exit_velocity * np.sin(launch_angle * DEG_TO_RAD)

    x = 0
    y = 0

    y_next = y + DT * v_y
    while(y_next > 0):
        y = y_next
        x = x + DT * v_x
        v_y = v_y - g * DT
        y_next = y + DT * v_y

    return [M_TO_FT * x, M_TO_FT * y]



delta_g = 0.0017 # goal is to get a 1 foot difference
print(distance_no_drag(9.8))
print(distance_no_drag(9.8*(1+delta_g)))




