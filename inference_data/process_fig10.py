import pdb
import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

rmc_list = ['rmc1', 'rmc2', 'rmc3']
lat_list = {}
throughput = {}

for rmc in rmc_list:
    lat_list[rmc] = []
    throughput[rmc] = []
    for i in range(2,15):
        with open(rmc+'_col/'+rmc+'_'+str(i)+'.json') as f:
            read = json.load(f)
        read = read[3:]
        mean = np.mean(read)
        lat_list[rmc].append(mean)
        thpt = 1000 * i / mean
        throughput[rmc].append(thpt)

########## plotting #############

#x = np.arange(len(rmc_list))  # the label locations
#width = 0.2  # the width of the bars
for rmc in rmc_list:
    fig, ax1 = plt.subplots(1,1)#,figsize=(12,5))
    ax1.plot(throughput[rmc], lat_list[rmc], 'bo-')

    ax1.set_ylabel('Latency (ms)')
    ##ax1.set_ylim(0,5)
    ax1.set_xlabel('throughput (inferences/s)')
    ax1.set_title(rmc + ' colocation from N=2 to N=14 on Broadwell CPU')
    plt.savefig('fig10/'+rmc+'.png')


#ax1.set_xticks(x)
#ax1.set_xticklabels(rmc_list)
#ax1.legend()
#ax1.grid(axis='y', linestyle=':', color='black')
#

#plt.show()

