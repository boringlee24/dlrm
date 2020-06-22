#!/bin/bash

cd ../

if [[ $# == 4 ]]; then
    extra_option=$4
else
    extra_option=""
fi

dlrm_pt_bin="python bkgd_pytorch.py"

rmc1_arg="--arch-mlp-bot=256-128-64 --arch-mlp-top=128-64-1 \
--arch-embedding-size=500000-500000-500000-500000-500000-500000-500000-500000-500000-500000-500000-500000-500000-500000-500000-500000-500000-500000-500000-\
500000-500000-500000-500000-500000-500000-500000-500000-500000-500000-500000-500000-500000 --arch-sparse-feature-size=64 \
--num-indices-per-lookup-fixed=True --num-indices-per-lookup=120 --arch-interaction-op=cat"
arguments="--data-generation=random --numpy-rand-seed=727 --print-freq=1 --print-time \
--inference-only"
numa_cmd="numactl --physcpubind=$3"


echo "run pytorch ..."
# WARNING: the following parameters will be set based on the data set
# --arch-embedding-size=... (sparse feature sizes)
# --arch-mlp-bot=... (the input to the first layer of bottom mlp)
cmd="$numa_cmd $dlrm_pt_bin $rmc1_arg $arguments --mini-batch-size=$1 --num-batches=$2 $extra_option"
echo "$cmd"
$cmd

echo "done"
