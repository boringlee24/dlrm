import pdb
import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

rmc_list = ['rmc1', 'rmc2_new4', 'rmc2_new1', 'rmc2_new3', 'rmc2_new2']
configs = ['cfg1', 'cfg2', 'cfg3', 'cfg4', 'cfg5']

no_col = []
for rmc in rmc_list:
    with open('rmc/'+rmc+'.json') as f:
        read = json.load(f)
    read = read[3:]
    mean = np.mean(read)
    cov = np.std(read) / mean * 100
    no_col.append(mean)
no_col = np.asarray(no_col)

col2 = []
for rmc in rmc_list:
    with open('rmc_col2/'+rmc+'.json') as f:
        read = json.load(f)
    read = read[3:]
    mean = np.mean(read)
    cov = np.std(read) / mean * 100
    col2.append(mean)
col2 = np.asarray(col2)

col4 = []
for rmc in rmc_list:
    with open('rmc_col4/'+rmc+'.json') as f:
        read = json.load(f)
    read = read[3:]
    mean = np.mean(read)
    cov = np.std(read) / mean * 100
    col4.append(mean)
col4 = np.asarray(col4)

col8 = []
for rmc in rmc_list:
    with open('rmc_col8/'+rmc+'.json') as f:
        read = json.load(f)
    read = read[3:]
    mean = np.mean(read)
    cov = np.std(read) / mean * 100
    col8.append(mean)
col8 = np.asarray(col8)

no_col_norm = no_col / no_col
col2_norm = col2 / no_col
col4_norm = col4 / no_col
col8_norm = col8 / no_col

pdb.set_trace()

########## plotting #############

x = np.arange(len(rmc_list))  # the label locations
width = 0.2  # the width of the bars

fig, ax1 = plt.subplots(1,1)#,figsize=(12,5))
ax1.bar(x - 3*width/2, no_col_norm, width, label='N=1')
ax1.bar(x - width/2, col2_norm, width, label='N=2')
ax1.bar(x + width/2, col4_norm, width, label='N=4')
ax1.bar(x + 3*width/2, col8_norm, width, label='N=8')

ax1.set_ylabel('Latency normalized to N=1')
#ax1.set_ylim(0,5)
ax1.set_xlabel('model')
ax1.set_title('Impact of co-colocation')
ax1.set_xticks(x)
ax1.set_xticklabels(configs)
ax1.legend()
ax1.grid(axis='y', linestyle=':', color='black')

#plt.show()
plt.savefig('fig9.png')


