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


# Fig: rav_comparison_no_drag.png
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

# Fig: grav_comparison_quad_drag.png
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

# Fig: grav_and_launch_angle_dependence_qd.png
# Generate figure to show how launch angle affects dependence of distance on gravity
labels = ["min", "mean", "max"]
colors = ["green", "dodgerblue", "orange"]
g_vals = parks[grav_col].describe()[labels].values
# range of launch angles for a ball hit at 100 mph to be conssidered a barrel
launch_angles = np.linspace(24, 33, num = (33-24)*2+1) 
distances = np.zeros([g_vals.size, launch_angles.size])

for i, g_val in enumerate(g_vals):
    for j, angle in enumerate(launch_angles):
        distances[i, j] = distance_quad_drag(g_val, launch_angle=angle)[0]

fig, axs = plt.subplots(2, 1, sharex=True)
for i, row in enumerate(distances):
    axs[0].scatter(launch_angles, row, c=colors[i], label=f"{labels[i]}={g_vals[i]:.3f}")
# subtract mean from min and max to plot the difference
distances[0, :] -= distances[1, :]
distances[2, :] -= distances[1, :]
axs[1].scatter(launch_angles, distances[0, :], c = colors[0])
axs[1].scatter(launch_angles, distances[2, :], c = colors[2])

for ax in axs:
    ax.grid(visible=True)
    ax.set_xlim(left= launch_angles[0] -0.1, right=launch_angles[-1] +0.1)
    ax.set_xticks(ticks=np.arange(launch_angles[0], launch_angles[-1]+1))
axs[0].set_ylabel("Distance (feet)")
axs[1].set_ylabel("Difference from Mean(feet)")
axs[1].set_xlabel("Launch Angle (degrees)")
axs[0].legend()
fig.set_size_inches(20.5, 10.5)
plt.subplots_adjust(hspace=0)
fig.savefig("baseball/figs/grav_and_launch_angle_dependence_qd.png", dpi=100)