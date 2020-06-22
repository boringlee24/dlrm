import pdb
import json
import numpy as np

#batch_list = ['64', '128', '256', '512']
#
#for batch in batch_list:
#    with open('batch_size/'+batch+'_0-11.json') as f:
#        read = json.load(f)
#    
#    median = round(np.median(read),3)
#    cov = round(np.std(read) / np.mean(read) * 100,3)
#    pct99 = round(np.percentile(read,99),3)
#    print(batch) 
#    print(median,',', cov,',', pct99)

#batch_list = ['diff', 'ht', 'same', 'small']
#
#for batch in batch_list:
#    with open('colocation/64_'+batch+'_2.json') as f:
#        read = json.load(f)
#    
#    median = round(np.median(read),3)
#    cov = round(np.std(read) / np.mean(read) * 100,3)
#    pct99 = round(np.percentile(read,99),3)
#    print(batch) 
#    print(median,',', cov,',', pct99)
#
#for batch in batch_list:
#    with open('colocation/256_'+batch+'_2.json') as f:
#        read = json.load(f)
#    
#    median = round(np.median(read),3)
#    cov = round(np.std(read) / np.mean(read) * 100,3)
#    pct99 = round(np.percentile(read,99),3)
#    print(batch) 
#    print(median,',', cov,',', pct99)
#
batch_list = ['K80', 'P100', 'V100']

for batch in batch_list:
    with open('gpu/'+batch+'_512.json') as f:
        read = json.load(f)
    # first inference is extremely slow
    read = read[1:] 
    median = round(np.median(read),3)
    cov = round(np.std(read) / np.mean(read) * 100,3)
    pct99 = round(np.percentile(read,99),3)
    print(batch) 
    print(median,',', cov,',', pct99)

