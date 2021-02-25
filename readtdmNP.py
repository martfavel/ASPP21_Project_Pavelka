import numpy as np
from nptdms import TdmsFile
import os



# Set-Location -Path D:\Uni\7th year\Advanced Python\Project

path = os.getcwd()
print(path)
filepath=str(path)+'\Data\\run030.tdms'
tdms_file = TdmsFile.read(filepath)

traces=[]

all_groups = tdms_file.groups()

print(all_groups[0])

mygroup = tdms_file['Time Trace']

all_group_channels = mygroup.channels()
all_group_channels

moving=mygroup['moving']
delay=mygroup['delay/ps']
intensity=mygroup['Intensity/nA']


import matplotlib.pyplot as plt 
  
rat=int(len(delay)/len(moving))
plt.plot(delay[0:rat], intensity[0:rat]) 
plt.show() 

# a=delay[0:rat]
# b=delay[rat:(rat)*2]
# c=delay[rat*160:rat*161]
# b==c

# a=intensity[0:rat]
# b=intensity[rat:(rat)*2]
# c=intensity[rat*3:rat*4]
# a==c
# # get number of groups

# group = tdms_file['Time Trace 1']
# channel = group['delay/ps']
# channel_data = channel[:]
# channel_properties = channel.properties

# for i in range (1,90):
#       group = tdms_file['Time Trace '+str(i)]
#       channel = group['Intensity/nA']
#       channel_data = channel[:]
#       channel_properties = channel.properties
#       traces.append(channel[:])
#       print('Time Trace '+str(i)+' loaded')
       
# averages=[]     
# averages=np.average(traces)
      
# 2d plot
      
      
# Average
      
      
# make spectrogram
      
      
# make spectrogram with different numbers of averages (box, gaussian and half-gaussian)
