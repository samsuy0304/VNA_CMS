import os
from optparse import OptionParser
import pandas as pd
import skrf as rf
from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib import style
import pickle as pl
import csv

cable_number = ""
cable_length = ""
cable_type = 0
t1 = 0
t2 = 0
Pre_list = []

y_plot_value=[]

comps = ['11','12', '21']
subfiles = ['0','0','1',]


    
# for i in range(1,len(Pre_list)+1):
#     ff["ff{i}".format(i)]= f"Data/"+cable_number+f"/{Pre_list[i-1]}"
#     filenames["filename{i}".format(i)]= f"{Pre_list[i-1]}"
# print(filenames)

def name(x):
    return x.strip(".vna").replace('Data/'+str(config.cable_number)+'/Plots/s2p/', "").strip("TP_")

y_plot_value=[]
def display_mean_impedance(ax, t1, t2, col):##https://www.tutorialfor.com/questions-285739.htm

    lines = ax.get_lines()

    # delete any other array correponding to a line drawn in ax but the last one. This is a
    # brute force way of resetting the line data to the data current line
    if len(lines)>1:
        del lines[:-1]

    # ressure that length of line is 1.
    #print('size of lines:', len(lines))

    # store the line arrays into list. Every line drawn on the ax is considered as data
    Y = [line.get_ydata() for line in lines]
    X = [line.get_xdata() for line in lines]

    # create a table, and since the list X and Y should have size=1, place the first
    # element (array) in pandas table columns t and Z
    df = pd.DataFrame()
    df['t'] = X[0]
    df['Z'] = Y[0]

    # get the mean value of Z for a given time difference
    Z_mean =  df.query('t >=@t1 & t<=@t2').agg({'Z': 'mean'})
    print('Mean impedance from', t1, 'ns and', t2, 'ns =', Z_mean.values, 'for', lines[0])
    # plot the average line
    x_coor = [t1, t2]
    y_coor = [Z_mean, Z_mean]
    y_plot_value.append(int(Z_mean.values))
    ax.plot(x_coor, y_coor, color=col, linewidth=1, label='', linestyle='--')

def set_axes(ax, title, ymin, ymax, xmin, xmax, nolim):
    ax.xaxis.set_minor_locator(AutoMinorLocator(2))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))
    ax.grid(True, color='0.8', which='minor')
    ax.grid(True, color='0.4', which='major')
    ax.set_title(title) #Time domain
    if nolim==False:
        ax.set_xlim((xmin, xmax))
        ax.set_ylim((ymin, ymax))
    plt.tight_layout()

