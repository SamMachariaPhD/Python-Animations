# Import the needed libraries. 

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec 
import matplotlib.patheffects as path_effects 

plt.style.use("ggplot")
cm = 1/2.54

# Create a time array. 
t_0 = 0; t_end = 2; t_dt = 0.005; 
t = np.arange(t_0, t_end+t_dt, t_dt) # [hrs] 
#print(t)

# Create x array. 
x = 800*t # [kms]
#print(x)
#plt.plot(t,x)
#plt.show()

# Create an array for y (altitude)
alt_0 = 2; alt_end = 2; 
y = np.linspace(alt_0, alt_end, len(x)) # "[0]" index at the end or "y, =" should give the 1st element
#print(y)
#exit()


# Create the animation 

fig0 = plt.figure(figsize=(40*cm,20*cm), dpi=120) # facecolor=(.8, .8, .8)
#fig1 = plt.figure(figsize=(18*cm,18*cm))
#fig3 = plt.figure(figsize=(18*cm,18*cm))
gs = gridspec.GridSpec(2,2)

ax0 = fig0.add_subplot(gs[0,:]); plt.xlim(x[0], x[-1]); plt.ylim(0,y[-1]+1); plt.xlabel("Distance (km)"); plt.ylabel("Altitude (km)") # facecolor
ax1 = fig0.add_subplot(gs[1,0]); plt.xlim(x[0], x[-1]); plt.ylim(0,y[-1]+1); plt.xlabel("Distance (km)"); plt.ylabel("Altitude (km)")
ax2 = fig0.add_subplot(gs[1,1]); plt.xlim(t[0], t[-1]); plt.ylim(0,x[-1]+1); plt.xlabel("Time (hr)"); plt.ylabel("Distance (km)")
trajectory0 = ax0.plot([],[], ls='-.')[0]
trajectory1 = ax1.plot([],[])[0]
trajectory2 = ax2.plot([],[])[0]

l0 = ax0.plot([],[], ls='-', lw=10, path_effects=[path_effects.SimpleLineShadow(), path_effects.Normal()])[0]

def animate(frame): # update plots
    trajectory0.set_data(x[0:frame], y[0:frame])
    trajectory1.set_data(x[0:frame], y[0:frame])
    trajectory2.set_data(t[0:frame], x[0:frame])
    l0.set_data([0+x[frame],20+x[frame]],[2,2])
    return trajectory0, trajectory1, trajectory2, l0

animation.FuncAnimation(fig0, animate, frames=len(t), interval=20, repeat=True, blit=True) # blit should be true for faster fig0 update
plt.show()