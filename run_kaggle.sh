num_batch=1000
cores="0-11"

for batch in 64 128 256 512
do
    json_path="inference_data/batch_size/${batch}_${cores}.json"   
    ./kaggle.sh $batch $num_batch $json_path $cores
    sleep 10
done

batch=256

for cores in 0-3 0-7 0,1,24,25 0-3,24-27 0-11,24-35
do
    json_path="inference_data/core_num/${batch}_${cores}.json"   
    ./kaggle.sh $batch $num_batch $json_path $cores
    sleep 10
done

