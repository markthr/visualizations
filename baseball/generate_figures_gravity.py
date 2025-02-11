import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from baseball_dynamics import distance_no_drag
from baseball_dynamics import distance_quad_drag


#--------------------------------------------------------------
#   Computer how an example barreled ball travels in different
#   ballparks without air resistance and with equalized air
#   with a quadratic drag model
#--------------------------------------------------------------

grav_col = "Gravity Mathematica"
bbd_vac_col = "Barreled Ball Distance No Drag" # traveling in a vacuum
bbd_qd_col = "Barreled Ball Distance With Quad Drag"
parks = pd.read_csv("baseball/data/Ballparks_With_Gravity.csv")

parks = parks.loc[parks["Major League"]] # only look at major league ballparks
parks[bbd_vac_col] = parks.apply(lambda row: distance_no_drag(row[grav_col])[0], axis=1)
parks[bbd_qd_col] = parks.apply(lambda row: distance_quad_drag(row[grav_col])[0], axis=1)


# Generate figure for ball without drag
fig, ax = plt.subplots()
ax.barh(parks.index, parks[bbd_vac_col])
ax.set_yticks(parks.index, parks["Ballpark"])
ax.set_xlim(left= 547, right=549)
ax.set_xlabel("Distance (feet)")
ax.set_title("Barreled ball distance by park without air resistance")
ax.grid(visible=True)
fig.set_size_inches(20.5, 10.5)
fig.savefig("baseball/figs/grav_comparison_no_drag.png", dpi=100)

# Generate figure for ball with drag
fig, ax = plt.subplots()
ax.barh(parks.index, parks[bbd_qd_col])
ax.set_yticks(parks.index, parks["Ballpark"])
ax.set_xlim(left= 348.5, right=350.5)
ax.set_xlabel("Distance (feet)")
ax.set_title("Barreled ball distance by park with quadratic air resistance")
ax.grid(visible=True)
fig.set_size_inches(20.5, 10.5)
fig.savefig("baseball/figs/grav_comparison_quad_drag.png", dpi=100)