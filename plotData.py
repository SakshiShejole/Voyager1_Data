import pylab as plt
from blimpy import Waterfall

%matlab inline

#Reading Voyager 1 data 

file_name = Waterfall('/path/to/file')
file_name.info()
data=file_name.data
print(data.shape)
print(data)

#plotting data

file_name.plot_spectrum(f_start=8419.2740, f_stop=8419.2750)

file_name.plot_waterfall(f_start=8419.2740, f_stop=8419.2750)


