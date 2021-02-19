My project for the course will aim at handling high performance data file fomats, primarily TDMS and secondly HDF5. My goal will be to be able to use both file formats as an input to my analysis code, being followed by representation in efficient data structure within the analysis code and some initial analysis would plot my test data into a 2D plot.

Update 01:

The code will first import TDMS file data. These data will be then categorized with pandas. As output, basic 2D graph will be created, accompanied by 1D graphs of some of accompanying metadata. This graph together with further data processing (such as Fourier transform and statistical treatement) will be saved in a hdf5 file.
