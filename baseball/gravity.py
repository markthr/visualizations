import numpy as np

MPH_TO_MPS = 0.44704
MPS_TO_MPH = 2.23694
DEG_TO_RAD = np.pi / 180
RAD_TO_DEG = 180 / np.pi
M_TO_FT = 3.28084
DT = 0.001

M = 0.146 # mass of a baseball (kg)
RHO = 1.225 # density of air (kg/m3)
R = 3.69 # radius of a baseball (cm)


# Model 1: No Drag, No Lift
def distance_no_drag(g, launch_angle = 27.5, exit_velocity = 100):
    dist_coeff = 0.5 * DT # coefficient for updating trapezoidal sum

    v_x = MPH_TO_MPS * exit_velocity * np.cos(launch_angle * DEG_TO_RAD)
    v_y = MPH_TO_MPS * exit_velocity * np.sin(launch_angle * DEG_TO_RAD)

    x = 0
    y = 0

    y_next = y + DT * v_y
    while(y_next > 0):
        # update positions
        x = x + DT * v_x
        y = y_next
        
        
        # update velocities
        v_y_prev = v_y
        v_y = v_y - g * DT
        # set y_next
        y_next = y + dist_coeff * (v_y + v_y_prev)

    return [M_TO_FT * x, M_TO_FT * y]

# Model 2: Quadratic Drag, No Lift
def distance_quad_drag(g, C_d = 0.3, launch_angle = 27.5, exit_velocity = 100):
    drag_coeff = 0.5 * RHO * np.pi * np.square(R*0.01) * C_d / M # scaling factor for v^2 in simple drag model
    dist_coeff = 0.5 * DT # coefficient for updating trapezoidal sum

    v = MPH_TO_MPS * exit_velocity
    angle = launch_angle * DEG_TO_RAD
    
    v_x = v * np.cos(angle)
    v_y = v * np.sin(angle)

    x = 0
    y = 0

    x_next = x + DT * v_x
    y_next = y + DT * v_y

    while(y_next > 0):
        # update positions
        x = x_next
        y = y_next
        # update velocity
        v_x_prev = v_x
        v_y_prev = v_y
        f_d = drag_coeff * np.square(v)
        v_x = v_x - np.cos(angle) * f_d * DT
        v_y = v_y - (g + np.sin(angle) * f_d) * DT
        v = np.sqrt(np.square(v_x) + np.square(v_y))
        angle = np.arctan(v_y / v_x)

        # set y_next
        y_next = y + dist_coeff * (v_y + v_y_prev)
        x_next = x + dist_coeff * (v_x + v_x_prev)

    return [M_TO_FT * x, M_TO_FT * y]

# Simple no drag model
delta_g = 0.002 # goal is to get a 1 foot difference
print(f"No air resistance model, delta_g={delta_g}")
print(distance_no_drag(9.8))
print(distance_no_drag(9.8*(1+delta_g)))

# Quadratic Drag Model
delta_g = 0.005 # goal is to get a 1 foot difference
print(f"Quadratic drag model, delta_g={delta_g}")
print(distance_quad_drag(9.8))
print(distance_quad_drag(9.8*(1+delta_g)))

