#-*- coding: utf-8 -*-
import numpy as np

#########################
## Suppose that we have to derive the relationship between pressure P(z) of an isothermal 
## ideal gas at some height z to pressure P(0) of this gas at height z=0. Each molecule of this gas ## with mass m experiences the acceleration of gravity g. This relationship is the well-known 
## barometric formula:
##   P(z)=P(0) exp(-m g z/kT)
## where g is the acceleration, k is the Boltzmann constant and T denotes temperature.
##  The ideal gas law relates the pressure P to gas density C as follows: 
## P(z)=C(z) kT. 
## Here C=N/V where N is number of molecules and V denotes  the volume of the gas. We can think of
## an ideal gas closed in a container which has a volume V. Equally we could write the barometric 
## formula for gas density as follows: C(z)=C(0)exp(-m g z/kT).
## In computer programm we will use dimensionless variables. If z=n[z0], where [z0] represents
## respective unit of z, and C0 is some reference value of the gas density which we put to
## be equal to 1, then G= m g [z0]/kT is dimensionless.
##
## We consider an ideal 1D gas along z-axis (gravity direction axis).
## It consists of N=1000 molecules which are enclosed in a container with dimension z=1 in units [z0]
## such that each gas molecule can move only in an interval [0,1]. 


rnd_start=2		#initial value for random number generator
np.random.seed(rnd_start)	#command to set this initial value
N=1000       #number of molecules in a 1D container

G=2.5   #dimensionless constant
L=1.0   #dimension of an initial box containing ideal gas molecules
nt=1000    #number of time steps of the experiment
dz=0.1    #assumed size of a molecule jump, it. can be some small value.


### Probability that a molecule moves up against gravity is equal to Probab_up=const*exp(-G*dz)
### The energy dE change is G*dz

##initiate an array representing locations of N molecules in a box of size L
z=np.zeros((N),dtype=np.float32) #z-locations of molecules location; 

for i in range(N):	#fill box rndomly with ideal gas molecules 
	z[i]=np.random.random()*L

	
for n in range(nt):
	#print("time ",n)
	for i in range(N): #take N molecules randomly (one Monte Carlo step)
		im=np.int32(np.random.rand()*N)
		height=z[im]
		r=np.random.rand()   #r is standard random number from [0,1); if r<0.5 try go up else try go down
		if r<0.5:
			Delta_E=G*dz
			height=height+dz
		else:
			Delta_E=-G*dz
			height=height-dz
		
		if Delta_E<0.0:
			if height>0.0 and height<L:		#check if molecule is in the box range
				z[im]=height
		else:
			rnd=np.random.rand() 
			if rnd<np.exp(-Delta_E):
				if height>0.0 and height<L: #check if molecule is in the box range
					z[im]=height

## After time nt passed make histogram of molecules location:
################ save to file dane.dat and check whether the exponential law takes place ###################
         
f0 = open("dane.dat", "w")
nbins=50
hist, bins = np.histogram(z,bins=nbins)
c0=hist[0]/np.float32(N)
for i in range(nbins):
	#print bins[i]," ",hist[i]  
	c=hist[i]/np.float32(N)
	strb=str(bins[i])+" "+str(c)+" "+str(c0*np.exp(-G*bins[i]))+"\n"
	f0.write(strb)
f0.close()
