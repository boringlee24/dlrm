import pdb
import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

log_path = '/home/li.baol/GIT/dlrm/inference_data/colocation/64_bkgd/half/'

batch_list = ['64', '128', '256', '512']
median_ls1 = []
mean_ls1 = []
tail_ls1 = []
median_ls2 = []
mean_ls2 = []
tail_ls2 = []

for batch in batch_list:
    with open(log_path+batch+'_diff_1.json') as f:
        read = json.load(f)
    # first inference is extremely slow
    # read = read[1:] 
    median_ls1.append(round(np.median(read),3))
    mean_ls1.append((round(np.mean(read),3)))
    tail_ls1.append(round(np.percentile(read,95),3))

    with open(log_path+batch+'_diff_2.json') as f:
        read = json.load(f)
    # first inference is extremely slow
    # read = read[1:] 
    median_ls2.append(round(np.median(read),3))
    mean_ls2.append((round(np.mean(read),3)))
    tail_ls2.append(round(np.percentile(read,95),3))

log_path = '/home/li.baol/GIT/dlrm/inference_data/colocation/64_bkgd/empty/'
median_base1 = []
mean_base1 = []
tail_base1 = []
median_base2 = []
mean_base2 = []
tail_base2 = []

for batch in batch_list:
    with open(log_path+batch+'_diff_1.json') as f:
        read = json.load(f)
    # first inference is extremely slow
    # read = read[1:] 
    median_base1.append(round(np.median(read),3))
    mean_base1.append((round(np.mean(read),3)))
    tail_base1.append(round(np.percentile(read,95),3))

    with open(log_path+batch+'_diff_2.json') as f:
        read = json.load(f)
    # first inference is extremely slow
    # read = read[1:] 
    median_base2.append(round(np.median(read),3))
    mean_base2.append((round(np.mean(read),3)))
    tail_base2.append(round(np.percentile(read,95),3))

median_ls1 = np.asarray(median_ls1)
mean_ls1 = np.asarray(mean_ls1)
tail_ls1 = np.asarray(tail_ls1)
median_base1 = np.asarray(median_base1)
mean_base1 = np.asarray(mean_base1)
tail_base1 = np.asarray(tail_base1)

median_ls2 = np.asarray(median_ls2)
mean_ls2 = np.asarray(mean_ls2)
tail_ls2 = np.asarray(tail_ls2)
median_base2 = np.asarray(median_base2)
mean_base2 = np.asarray(mean_base2)
tail_base2 = np.asarray(tail_base2)

median_norm1 = median_ls1 / median_base1
mean_norm1 = mean_ls1 / mean_base1
tail_norm1 = tail_ls1 / tail_base1
median_norm2 = median_ls2 / median_base2
mean_norm2 = mean_ls2 / mean_base2
tail_norm2 = tail_ls2 / tail_base2

############## plotting ################

x = np.arange(len(batch_list))  # the label locations
width = 0.2  # the width of the bars

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(12,5))
ax1.bar(x - width, mean_norm1, width, label='mean')
ax1.bar(x, median_norm1, width, label='median')
ax1.bar(x + width, tail_norm1, width, label='95th tail')

ax1.set_ylabel('Normalized value (lower is better)')
ax1.set_ylim(0,5)
ax1.set_xlabel('batch size')
ax1.set_title('Background process using same cpu')
ax1.set_xticks(x)
ax1.set_xticklabels(batch_list)
#ax1.legend()
ax1.grid(axis='y', linestyle=':', color='black')

ax2.bar(x - width, mean_norm2, width, label='mean')
ax2.bar(x, median_norm2, width, label='median')
ax2.bar(x + width, tail_norm2, width, label='95th tail')

ax2.set_ylabel('Normalized value (lower is better)')
ax2.set_ylim(0,5)
ax2.set_xlabel('batch size')
ax2.set_title('Background process using diff cpu')
ax2.set_xticks(x)
ax2.set_xticklabels(batch_list)
ax2.legend()
ax2.grid(axis='y', linestyle=':', color='black')

#plt.show()
plt.savefig('plot2.png')
