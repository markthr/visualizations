import pandas as pd
from baseball_dynamics import distance_no_drag
from baseball_dynamics import distance_quad_drag

#--------------------------------------------------------------
#   Check how a small change in gravity affects the distance a
#   baseball travels.
#--------------------------------------------------------------

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
print()

#--------------------------------------------------------------
#   Observe how much gravity varies for each ballpark in the
#   Mathematica sourced gravity figures
#--------------------------------------------------------------

grav_col = "Gravity Mathematica"
parks = pd.read_csv("baseball/data/Ballparks_With_Gravity.csv")

parks = parks.loc[parks["Major League"]].sort_values(by=[grav_col])

grav_avg = parks[grav_col].mean()
print(f"Average gravity: {grav_avg}")

print(parks[grav_col].iloc[-1])
print(f"Min gravity: {parks[grav_col].iloc[0]} ({(parks[grav_col].iloc[0]-grav_avg)*100/grav_avg:{3}.{3}}%)")
print(f"Max gravity: {parks[grav_col].iloc[-1]} (+{(parks[grav_col].iloc[-1]-grav_avg)*100/grav_avg:{3}.{3}}%)")

# A 0.2% difference in gravity is enough to get a 1 foot difference on a barreled ball in a vacuum
# However, a 0.5% difference is needed when modeling air resistance with a simple quadratic drag model
# The real answer, is somewhere in between given the drag crisis
