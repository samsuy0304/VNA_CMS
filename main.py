# Importing modules
import os
from optparse import OptionParser
import pandas as pd
import skrf as rf
from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib import style

# Import other classes
import config

config.cable_length = str(input("What is the cable length [35, 80, 100, 140, 160, 200]: "))
config.cable_number = str(input("What is the cable number: "))
config.cable_type = int(input("What is the cable type [1,2,3,4]: "))
redo = int(input("Redo s2p files [1 Yes, 0 No]: "))



print("\n Detecting Files...")
for root, dirs, files in os.walk("./Data/"+config.cable_number, topdown=False):
   for name in files:
      if ".txt" in os.path.join(name):
        config.Pre_list.append(os.path.join(name))



print(" Files detected")
print(config.Pre_list)

if len(os.path.join('Data/'+str(config.cable_number)+'/Plots/s2p')) == 0:
    import createS2P
elif redo == 1:
    import createS2P
elif redo == 0:
    pass


if config.cable_length == "35":
    config.t1 = 2.00
    config.t2 = 4.00
elif config.cable_length == "80":
    config.t1 = 2.00
    config.t2 = 6.00
elif config.cable_length == "100":
    config.t1 = 2.00
    config.t2 = 7.00
elif config.cable_length == "140":
    config.t1 = 2.00
    config.t2 = 9.00
elif config.cable_length == "160":
    config.t1 = 2.00
    config.t2 = 10.00
elif config.cable_length == "180":
    config.t1 = 2.00
    config.t2 = 11.00
elif config.cable_length == "200":
    config.t1 = 2.00
    config.t2 = 12.00
elif config.cable_length == "0":
    config.t1 = 0.00
    config.t2 = 1.50
else:
    config.t1=0
    config.t2=0

try:
    if config.cable_type == 1:
        import type1
    elif config.cable_type == 2:
        import type2
    elif config.cable_type == 3:
        import type3
    elif config.cable_type == 4:
        import type4
except NameError:
    print("Files Not Detected!!")
