
# Importing packages

import numpy as np
from nptdms import TdmsFile
import os
import matplotlib.pyplot as plt 
from datetime import datetime

# Measuring time it takes for the whole code to finish 

startTime = datetime.now()

#  Specyfying the location of the file

path = os.getcwd()
print(path)
filepath=str(path)+'\Data\\run030.tdms'


# Opening the file and selecting the group

tdms_file = TdmsFile.read(filepath)
all_groups = tdms_file.groups()

print(all_groups)

mygroup = tdms_file['Time Trace']

# Loading the separate channels

all_group_channels = mygroup.channels()
print(all_group_channels)

moving=mygroup['moving']
position=mygroup['position/mm']
humidity=mygroup['humidity']
delay=mygroup['delay/ps']
intensity=mygroup['Intensity/nA']
timestamp=mygroup['timestamp/ms']
averages=mygroup['averages']


#  Reshaping intensity values into matrix with consequtive "time traces" as rows
  
trace_lenght=int(len(delay)/len(moving))

intensity_values=intensity[:]
traces=intensity_values.reshape((len(moving),trace_lenght))

#  Plotting 2D graph of the raw data

plt.imshow(np.transpose(traces)+30, interpolation="nearest", origin="upper", aspect='auto')
plt.colorbar()
plt.show()
plt.close()

# Plotting the raw data together with metadata

f, (ax1, ax2,ax3) = plt.subplots(3,1, sharex=True)
ax1.plot(humidity)
ax2.plot(position)
ax3.imshow(np.transpose(traces)+30, interpolation="nearest", aspect='auto')
            # ,extent =[x.min(), x.max(),y.min(),y.max()])
            # , extent=[0, 1, 0, N])
            # , cmap="inferno"
# ax2.set_ylim(0, N)
# ax3.add_axes([0.7, 0.1, 0.05, 0.8])
ax3.set_aspect('auto')
ax1.set_ylabel("humidity")
ax2.set_ylabel("stage at")
ax3.set_ylabel("delay")
ax3.set_xlabel("time")
plt.show()
plt.close()


# Simple analysis of a single trace

y = traces[0]+25
# y = -traces[0]-35
x= delay[:trace_lenght]

from scipy.signal import find_peaks
from PyAstronomy import pyaC

plt.plot(x,y)

# Finding peaks

peaks, _ = find_peaks(y, height=0)
plt.plot((peaks*(x[1]-x[0])+x[0]), y[peaks], "x")
plt.plot(x,np.zeros_like(x), "--", color="gray")

# Finding zero-crossings

xc, xi = pyaC.zerocross1d(x, y, getIndices=True)
plt.plot(xc, np.zeros(len(xc)), 'kp')
plt.plot(x[xi], y[xi], 'gp')

plt.show()
plt.close()

# Now, let's save the data as HDF5 file

import h5py

hf = h5py.File('data.h5', 'w')
# hf = h5py.File('data.h5', 'r')

hf.create_dataset('Time traces', data=traces)
hf.create_dataset('moving', data=moving)
hf.create_dataset('humidity', data=humidity)
hf.create_dataset('delay/ps', data=delay)
hf.create_dataset('timestamp/ms', data=timestamp)
hf.create_dataset('averages', data=averages)


# Checking wheather the saving was sucesful

hf.keys()
n1 = hf.get('moving')
print(n1[:]==moving[:])

#  Group with processed data

g1 = hf.create_group('Processed')
g1.create_dataset('crossings',data=xc)
g1.create_dataset('peaks',data=y[peaks])

hf.close()

print(datetime.now() - startTime)


#  Here follows leftover code for future use

# for i in range(0,len(moving)):
#       print (i)
#       traces_intensities.append(intensity[trace_lenght*i:trace_lenght*(i+1)-cutoff])


# y=timestamp[:]/1000
# x=delay[0]

# plt.imshow(np.transpose(traces)+30, interpolation="nearest", origin="upper", aspect='auto')
# # ,extent =[x.min(), x.max(),y.min(),y.max()])
# plt.colorbar()
# plt.show()
# plt.close()


# plt.plot((timestamp-timestamp[0])/1000,position[:]) 
# plt.show() 
# plt.close()

# plt.plot(np.diff(timestamp)) 
# plt.show() 

# plt.plot(np.flip(traces[0]),delay[0:trace_lenght]) 
# plt.show() 

# a=delay[0:rat]
# b=delay[rat:(rat)*2]
# c=delay[rat*160:rat*161]
# b==c

# a=intensity[0:rat]
# b=intensity[rat:(rat)*2]
# c=intensity[rat*3:rat*4]
# a==c
