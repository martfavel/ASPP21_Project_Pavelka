import numpy as np
from nptdms import TdmsFile
import os



# Set-Location -Path D:\Uni\7th year\Advanced Python\Project

path = os.getcwd()
print(path)
filepath=str(path)+'\Sample data\\run030.tdms'
tdms_file = TdmsFile.read(filepath)

traces=[]

all_groups = tdms_file.groups()

print(all_groups[0])

mygroup = tdms_file['Time Trace']

all_group_channels = mygroup.channels()
all_group_channels

channel_moving=["moving"]
channel_moving
all_channel_data = channel_moving[:]
all_channel_data


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
