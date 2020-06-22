num_batch=1000
gpus=1
gpu_type="V100"

for batch in 64 128 256 512
do
    json_path="inference_data/gpu/${gpu_type}_${batch}.json"   
    ./kaggle_gpu.sh $batch $num_batch $json_path $gpus "--log-path=run_log/gpu/${gpu_type}_${batch}.json"
    sleep 10
done


