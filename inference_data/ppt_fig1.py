import pdb
import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

rmc_list = ['rmc1', 'rmc2_new1']
configs = ['model A', 'model B']

no_col = []
for rmc in rmc_list:
    with open('rmc/'+rmc+'.json') as f:
        read = json.load(f)
    read = read[3:]
    mean = np.mean(read)
    no_col.append(mean)
no_col = np.asarray(no_col)

col8 = []
for rmc in rmc_list:
    with open('rmc_col8/'+rmc+'.json') as f:
        read = json.load(f)
    read = read[3:]
    mean = np.mean(read)
    col8.append(mean)
col8 = np.asarray(col8)

col = []
for rmc in rmc_list:
    with open('col/'+rmc+'_4.json') as f:
        read = json.load(f)
    read = read[3:]
    mean = np.mean(read)
    col.append(mean)
col = np.asarray(col)
   
no_col_norm = no_col / no_col
col8_norm = col8 / no_col
col_norm = col / no_col

########## plotting #############

x = np.arange(len(rmc_list))  # the label locations
width = 0.2  # the width of the bars

fig, ax1 = plt.subplots(1,2)#,figsize=(12,5))
for ax in ax1:
    if ax == ax1[0]:
        ax.bar(x, col8_norm, width)
        ax.set_title('Config1')
    else:
        ax.bar(x, col_norm, width)
        ax.set_title('Config2')

    if ax == ax1[0]:
        ax.set_ylabel('Latency normalized to no colocation')
    ax.set_ylim(0,14)
    ax.set_yticks(np.arange(15))
    ax.set_xlabel('model')
    ax.set_xticks(x)
    ax.set_xticklabels(configs)
    #ax1.legend()
    ax.grid(axis='y', which='both', linestyle=':', color='black')

#plt.show()
plt.savefig('fig1.png')


