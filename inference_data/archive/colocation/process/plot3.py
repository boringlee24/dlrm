import pdb
import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

log_path = '/home/li.baol/GIT/dlrm/inference_data/colocation/0.5_64/'

with open(log_path+'64_half.json') as f:
    read = json.load(f)

############## plotting ################

fig, (ax) = plt.subplots(1,1,figsize=(12,5))
ax.plot(read)

ax.set_ylabel('inference latency (ms)')
#ax.set_xlim(0,30000)
ax.set_xlabel('processed query over time')
ax.set_title('Background inference latency over time')
#ax.set_xticks(x)
#ax.set_xticklabels(batch_list)
##ax.legend()
#ax.grid(axis='y', linestyle=':', color='black')

plt.show()
#plt.savefig('plot3.png')
