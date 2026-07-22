import numpy as np


seed = 2		#initial value for random number generator
np.random.seed(seed)	#command to set this initial value
N = 1000       #number of molecules in a 1D container

G = 2.5   #dimensionless constant
L = 1.0   #dimension of an initial box containing ideal gas molecules
nt = 1000    #number of time steps of the experiment
dz = 0.1    #assumed size of a molecule jump, it. can be some small value.

### Define an array C[] which will collect concentrations in each been from nbins of the
### histograms
### from different experiments (number of repeats of a single experiment)
nbins = 10
concentrations = np.zeros((nbins), dtype=np.float32)
concentrations_sqrd = np.zeros((nbins), dtype=np.float32) # this will collect squares of C[] to calculate standard deviation
D = np.zeros((nbins), dtype=np.float32)	#records distances z in a form of bins

### Probability that a molecule moves up against gravity is equal to Probab_up=const*exp(-G*dz)
### The energy Delta_E change is equal to G*dz

##initiate an array representing locations of N molecules in a box of size L
z = np.zeros((N), dtype=np.float32) #z-locations of molecules location; 

######################## We reorganize our program by introducing functions ##########
####################### The first one Fill_box() #############

def spawn_molecules(L, N):	#fill box randomly with ideal gas molecules 
	for i in range(N):	
		z[i] = np.random.random() * L

def run_single_experiment(nt, nbins, Naverages):	
	for _ in range(nt):
		for _ in range(N): #take N molecules randomly (one Monte Carlo step)
			im = np.int32(np.random.rand() * N)
			height = z[im]
			r = np.random.rand()   #r is standard random number from [0,1); if r<0.5 try go up else try go down
			if r < 0.5:
				Delta_E = G * dz
				height = height + dz
			else:
				Delta_E = -G * dz
				height = height - dz
		
			if Delta_E < 0.0:
				if height > 0.0 and height < L:		#check if molecule is in the box range
					z[im] = height
			else:
				rnd = np.random.rand() 
				if rnd < np.exp(-Delta_E):
					if height > 0.0 and height < L: #check if molecule is in the box range
						z[im] = height
		
	hist, bins = np.histogram(z, bins=nbins)	#make a histogram of distances z[]
	for i in range(nbins):
		density = hist[i] / np.float32(N)
		concentrations[i] += density / Naverages	#collect density data from this experiment
		concentrations_sqrd[i] += density * density / Naverages
		D[i] = bins[i]
		
################# MAIN SECTION ################################

	#Here we repeat the experiment Naverages times to calculate the averaged density of molecules
	
Naverages=10
for i in range(Naverages):
    print("#performing experiment ", i)
    spawn_molecules(L, N)	#filling box randomly with N gas molecules
    run_single_experiment(nt, nbins, Naverages)	#perform the Monte Carlo experiment 
                                        #with nt Monte Carlo steps 
##### save to file three-column data where the third one is 3 times standard deviation
f0 = open("dane2.dat", "w")
c0 = concentrations[0]
	
for i in range(nbins):
	density = concentrations[i]
	std_dev = np.sqrt(concentrations_sqrd[i] - concentrations[i] * concentrations[i])	#sigma, statistical error, often "3 sigma" is used
	strb = str(D[i]) + " " + str(density) + " " + str(3 * std_dev) + " " + str(c0 * np.exp(-G * D[i])) + "\n"
	f0.write(strb)
f0.close()
