#!/bin/bash

if [[ $# == 5 ]]; then
    extra_option=$5
else
    extra_option=""
fi

dlrm_pt_bin="python dlrm_s_pytorch.py"
arguments="--arch-sparse-feature-size=16 --arch-mlp-bot=13-512-256-64-16 --arch-mlp-top=512-256-1 \
--data-generation=dataset --data-set=kaggle --raw-data-file=/scratch/li.baol/Kaggle_dataset/train.txt \
--processed-data-file=/scratch/li.baol/Kaggle_dataset/kaggleAdDisplayChallenge_processed.npz \
--loss-function=bce --round-targets=True --learning-rate=0.1 --print-freq=1 --print-time \
--load-model=saved_model/kaggle.pt --inference-only --json-dump"
ngpus=$4
_gpus=$(seq -s, 0 $(($ngpus-1)))
cuda_arg="CUDA_VISIBLE_DEVICES=$_gpus"
echo $cuda_arg

echo "run pytorch ..."
# WARNING: the following parameters will be set based on the data set
# --arch-embedding-size=... (sparse feature sizes)
# --arch-mlp-bot=... (the input to the first layer of bottom mlp)
cmd="$cuda_arg $dlrm_pt_bin $arguments --mini-batch-size=$1 --num-batches=$2 --json-path=$3 --use-gpu $extra_option"
echo "$cmd"
eval $cmd

echo "done"
