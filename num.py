import numpy as np
t = np.linspace(0,10,100)
x = np.cos(t)
y = np.sin(t)
z = t/2

traj = np.column_stack((x,y,z))
print("Traj shape: ", traj.shape)
print("time ", t.shape)
print("Traj Size", traj.size)