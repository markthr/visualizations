import pandas as pd
import numpy as np

grav_col = "Gravity Mathematica"
parks = pd.read_csv("baseball/data/Ballparks_With_Gravity.csv")

parks = parks.loc[parks["Major League"]].sort_values(by=[grav_col])

print(parks[grav_col].values)
grav_avg = parks[grav_col].mean()
print(f"Average gravity: {grav_avg}")

print(parks[grav_col].iloc[-1])
print(f"Min gravity: {parks[grav_col].iloc[0]} ({(parks[grav_col].iloc[0]-grav_avg)*100/grav_avg:{3}.{3}}%)")
print(f"Max gravity: {parks[grav_col].iloc[-1]} (+{(parks[grav_col].iloc[-1]-grav_avg)*100/grav_avg:{3}.{3}}%)")

# A 0.2% difference in gravity is enough to get a 1 foot difference on a barreled ball in a vacuum
# However, a 0.5% difference is needed when modeling air resistance with a simple quadratic drag model
# The real answer, is somewhere in between given the drag crisis
