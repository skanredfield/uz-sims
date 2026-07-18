#-*- coding: utf-8 -*-
import numpy as np
#########################
# extended version where error bars calculation is added.
#We will make some number of repeats (Naverages) of the same experiment and will plot
#average value <N/V> = <c> = 1/Naverages \sum_{i=1}^N c_i where index i denotes different #experiments. We will calcutate standard deviation too and our error bars will have value of
# 3 sigme = 3  x standard deviation. 
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

### Define an array C[] which will collect concentrations in each been from nbins of the
### histograms
### from different experiments (number of repeats of a single experiment)
nbins=10
C=np.zeros((nbins),dtype=np.float32)
C2=np.zeros((nbins),dtype=np.float32) # this will collect squares of C[] to calculate standard deviation
D=np.zeros((nbins),dtype=np.float32)	#records distances z in a form of bins

### Probability that a molecule moves up against gravity is equal to Probab_up=const*exp(-G*dz)
### The energy Delta_E change is equal to G*dz

##initiate an array representing locations of N molecules in a box of size L
z=np.zeros((N),dtype=np.float32) #z-locations of molecules location; 

######################## We reorganize our program by introducing functions ##########
####################### The first one Fill_box() #############

def Fill_box(L,N):	#fill box randomly with ideal gas molecules 
	for i in range(N):	
		z[i]=np.random.random()*L

def single_experiment(nt,nbins,Naverages):	
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
		
	hist, bins = np.histogram(z,bins=nbins)	#make a histogram of distances z[]
	for i in range(nbins):
		density=hist[i]/np.float32(N)
		C[i]=C[i]+density/Naverages	#collect density data from this experiment
		C2[i]=C2[i]+density*density/Naverages
		D[i]=bins[i]
################# MAIN SECTION ################################
if __name__ == '__main__':    
	#Here we repeat the experiment Naverages times to calculate the averaged density of molecules
	
	Naverages=10
	for i in range(Naverages):
		print("#performing experiment ",i)
		Fill_box(L,N)	#filling box randomly with N gas molecules
		single_experiment(nt,nbins,Naverages)	#perform the Monte Carlo experiment 
											#with nt Monte Carlo steps 
	##### save to file three-column data where the third one is 3 times standard deviation
	f0 = open("dane2.dat", "w")
	c0=C[0]
for i in range(nbins):
	density=C[i]
	std_dev=np.sqrt(C2[i]-C[i]*C[i])	#sigma, statistical error, often "3 sigma" is used
	strb=str(D[i])+" "+str(density)+" "+str(3*std_dev)+" "+str(c0*np.exp(-G*D[i]))+"\n"
	f0.write(strb)
f0.close()
