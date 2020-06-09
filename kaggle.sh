
dlrm_pt_bin="python dlrm_s_pytorch.py"
arguments="--arch-sparse-feature-size=16 --arch-mlp-bot=13-512-256-64-16 --arch-mlp-top=512-256-1 \
--data-generation=dataset --data-set=kaggle --raw-data-file=/scratch/li.baol/Kaggle_dataset/train.txt \
--processed-data-file=/scratch/li.baol/Kaggle_dataset/kaggleAdDisplayChallenge_processed.npz \
--loss-function=bce --round-targets=True --learning-rate=0.1 --print-freq=1 --print-time \
--load-model=saved_model/kaggle.pt --inference-only --json-dump"
numa_cmd="numactl --physcpubind=$4"


echo "run pytorch ..."
# WARNING: the following parameters will be set based on the data set
# --arch-embedding-size=... (sparse feature sizes)
# --arch-mlp-bot=... (the input to the first layer of bottom mlp)
cmd="$numa_cmd $dlrm_pt_bin $arguments --mini-batch-size=$1 --num-batches=$2 --json-path=$3"
echo "$cmd"
$cmd

echo "done"
