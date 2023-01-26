import numpy as np
import matplotlib.pyplot as plt

# getting the road type and condition from the user to determine the friction coefficient

roadtype = input("Please input the road type:")
roadcondition = input ("Please input the road condition:")
fcoef = 0

if roadtype=="concrete" and roadcondition=="dry":
    fcoef = 0.5
elif roadtype=="concrete" and roadcondition=="wet":
    fcoef=0.35
elif roadtype=="ice" and roadcondition=="dry":
    fcoef=0.15
elif roadtype=="ice" and roadcondition=="wet":
    fcoef=0.08
elif roadtype=="gravel" and roadcondition=="dry":
    fcoef=0.35
elif roadtype=="sand" and roadcondition=="dry":
    fcoef=0.3
elif roadtype=="water":
    fcoef=0.05
else:
    print("Parameters entered are not valid")
    fcoef=0

# if the entered road parameters are valid, read the initial vehicle velocity and road inclination angle.
# road inclination angle is positive when car is going uphill and negative when going downhill

if fcoef!=0:
    velocity = float(input("Please input the initial velocity (in km/h) of the vehicle: "))
    theta = float(input("Please input the inclination angle (in degrees) with positive for uphill and negative for downhill: "))

# converting the vehicle initial velocity from km/h to m/s to use it in the distance calculation

    v0 = velocity/3.6

# converting the road inclination angle from degrees to radiant

    thetadeg = (theta*(np.pi))/180
    print (theta)
    print (thetadeg)
    print (np.sin(thetadeg))

# calculating the stopping distance by setting the work equilibrium between the works done by friction force
# , gravity force and the initial kinetic energy of the vehicle
# for an uphill situation the sin of the inclination angle (thetadeg) would be positive, leading to a larger
# denominator in the equation, leading to a smaller Sstop value, hence the gravitation force would help the
# braking. On the contrary, for a downhill situation the sin of thetadeg would be negative, decreasing the
# denominator value and leading to a higher Sstop, hence the gravitation force is acting against the braking.

    Sbraking = (v0**2)/(2*9.81*(fcoef*np.cos(thetadeg)+np.sin(thetadeg)))

# solving for the acceleration to stop and the time to stop by using a force balance:



    a = fcoef*9.81*np.cos(thetadeg)+9.81*np.sin(thetadeg)
    Tbraking = v0/a
    print (Tbraking)
    print (Sbraking)
    print (a)

# assuming a reaction time of 0.3 sec, the total time is 0.3 plus the braking time
# creating a linspace to represent braking time from Treaction to total stop time.

Treac = 0.3
Ttotal = Treac + Tbraking
time = np.linspace (Treac,Ttotal)

# calculating the velocity (in km/h) and distance for every instance of time using the calculated acceleration
# assuming a reaction time of 0.3 sec, the distance traveled until reaction is the reaction time multiplied
# by the initial velocity
# concatenating the reaction time with the braking time, and setting the velocity values in the reaction time
# to the initial velocity

tZero = [0]
time = np.concatenate([tZero, time])
s0 = 0.3 * v0
v = 3.6*(v0 - a*(time-Treac))
v[0] = velocity
s = s0 + v0*(time-Treac) + 0.5*a*((time-Treac)**2)

# plotting the velocity and distance traveled vs time starting at the braking instance until the full stop

fig, ax = plt.subplots(figsize = (10, 5))
plt.title('Distance & Velocity vs Time')

ax2 = ax.twinx()
ax.plot(time, s, color = 'g')
ax2.plot(time, v, color = 'b')

# naming the x axis
ax.set_xlabel('Time')
# naming the y axis
ax.set_ylabel('Distance in m', color = 'g')
ax2.set_ylabel('Velocity in km/h', color = 'b')


#annotating the values of distance at Treaction and at Ttotal
j=1
plt.annotate(str(s[j]), xy=(time[j], s[j]))
i = len(time)-1
plt.annotate(str(s[i]), xy=(time[i], s[i]))

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
