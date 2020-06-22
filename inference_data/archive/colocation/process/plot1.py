import pdb
import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

log_path = '/home/li.baol/GIT/dlrm/inference_data/colocation/64_bkgd/full/'

batch_list = ['64', '128', '256', '512']
median_ls = []
mean_ls = []
tail_ls = []

for batch in batch_list:
    with open(log_path+batch+'_same_1.json') as f:
        read = json.load(f)
    # first inference is extremely slow
    # read = read[1:] 
    median_ls.append(round(np.median(read),3))
    mean_ls.append((round(np.mean(read),3)))
    tail_ls.append(round(np.percentile(read,95),3))


log_path = '/home/li.baol/GIT/dlrm/inference_data/colocation/64_bkgd/empty/'
median_base = []
mean_base = []
tail_base = []

for batch in batch_list:
    with open(log_path+batch+'_same_1.json') as f:
        read = json.load(f)
    # first inference is extremely slow
    # read = read[1:] 
    median_base.append(round(np.median(read),3))
    mean_base.append((round(np.mean(read),3)))
    tail_base.append(round(np.percentile(read,95),3))

median_ls = np.asarray(median_ls)
mean_ls = np.asarray(mean_ls)
tail_ls = np.asarray(tail_ls)
median_base = np.asarray(median_base)
mean_base = np.asarray(mean_base)
tail_base = np.asarray(tail_base)

median_norm = median_ls / median_base
mean_norm = mean_ls / mean_base
tail_norm = tail_ls / tail_base

############## plotting ################

x = np.arange(len(batch_list))  # the label locations
width = 0.2  # the width of the bars

fig, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(14,5))
ax1.bar(x - width, mean_norm, width, label='mean')
ax1.bar(x, median_norm, width, label='median')
ax1.bar(x + width, tail_norm, width, label='95th tail')

ax1.set_ylabel('Normalized value (lower is better)')
ax1.set_ylim(0,5)
ax1.set_xlabel('batch size')
ax1.set_title('Background process 64 batch size')
ax1.set_xticks(x)
ax1.set_xticklabels(batch_list)
#ax1.legend()
ax1.grid(axis='y', linestyle=':', color='black')
#########################################

log_path = '/home/li.baol/GIT/dlrm/inference_data/colocation/256_bkgd/full/'
median_ls = []
mean_ls = []
tail_ls = []

for batch in batch_list:
    with open(log_path+batch+'_same_1.json') as f:
        read = json.load(f)
    # first inference is extremely slow
    # read = read[1:] 
    median_ls.append(round(np.median(read),3))
    mean_ls.append((round(np.mean(read),3)))
    tail_ls.append(round(np.percentile(read,95),3))
median_ls = np.asarray(median_ls)
mean_ls = np.asarray(mean_ls)
tail_ls = np.asarray(tail_ls)
median_norm = median_ls / median_base
mean_norm = mean_ls / mean_base
tail_norm = tail_ls / tail_base

ax2.bar(x - width, mean_norm, width, label='mean')
ax2.bar(x, median_norm, width, label='median')
ax2.bar(x + width, tail_norm, width, label='95th tail')

ax2.set_ylabel('Normalized value (lower is better)')
ax2.set_ylim(0,5)
ax2.set_xlabel('batch size')
ax2.set_title('Background process 256 batch size')
ax2.set_xticks(x)
ax2.set_xticklabels(batch_list)
#ax2.legend()
ax2.grid(axis='y', linestyle=':', color='black')

log_path = '/home/li.baol/GIT/dlrm/inference_data/colocation/0.5_64/full/'
median_ls = []
mean_ls = []
tail_ls = []

for batch in batch_list:
    with open(log_path+batch+'_same_1.json') as f:
        read = json.load(f)
    # first inference is extremely slow
    # read = read[1:] 
    median_ls.append(round(np.median(read),3))
    mean_ls.append((round(np.mean(read),3)))
    tail_ls.append(round(np.percentile(read,95),3))
median_ls = np.asarray(median_ls)
mean_ls = np.asarray(mean_ls)
tail_ls = np.asarray(tail_ls)
median_norm = median_ls / median_base
mean_norm = mean_ls / mean_base
tail_norm = tail_ls / tail_base

ax3.bar(x - width, mean_norm, width, label='mean')
ax3.bar(x, median_norm, width, label='median')
ax3.bar(x + width, tail_norm, width, label='95th tail')

ax3.set_ylabel('Normalized value (lower is better)')
ax3.set_ylim(0,5)
ax3.set_xlabel('batch size')
ax3.set_title('Background process 64 batch size at lower rate')
ax3.set_xticks(x)
ax3.set_xticklabels(batch_list)
ax3.legend()
ax3.grid(axis='y', linestyle=':', color='black')

#plt.show()
plt.savefig('plot1.png')
