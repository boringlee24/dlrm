#!/bin/bash

cd ../

if [[ $# == 5 ]]; then
    extra_option=$5
else
    extra_option=""
fi

dlrm_pt_bin="python dlrm_s_pytorch.py"

rmc1_arg="--arch-mlp-bot=128-64-32 --arch-mlp-top=256-64-1 \
--arch-embedding-size=4000000-4000000-4000000-4000000-4000000-4000000-4000000-4000000 --arch-sparse-feature-size=32 \
--num-indices-per-lookup-fixed=True --num-indices-per-lookup=80 --arch-interaction-op=cat"
arguments="--data-generation=random --numpy-rand-seed=727 --print-freq=1 --print-time \
--inference-only --json-dump"
numa_cmd="numactl --physcpubind=$4"


echo "run pytorch ..."
# WARNING: the following parameters will be set based on the data set
# --arch-embedding-size=... (sparse feature sizes)
# --arch-mlp-bot=... (the input to the first layer of bottom mlp)
cmd="$numa_cmd $dlrm_pt_bin $rmc1_arg $arguments --mini-batch-size=$1 --num-batches=$2 --json-path=$3 $extra_option"
echo "$cmd"
$cmd

echo "done"
