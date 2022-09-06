# Import the needed libraries. 
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec 
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
y = np.linspace(alt_0, alt_end, len(x))
#print(y)

# Create the animation 

frames = len(t)
fig = plt.figure(figsize=(40*cm,20*cm), dpi=120) # facecolor(.8, .8, .8)
anim = animation.FuncAnimation()