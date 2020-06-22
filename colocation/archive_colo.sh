num_batch=1000
cd ../

# colocation on different cpu config
# colocation of different batch size tasks

#for batch in 64 128 256 512
#do
#    json_path="inference_data/colocation/${batch}_diff_1.json"   
#    ./kaggle.sh $batch $num_batch $json_path "0-11" "--log-path=run_log/${batch}_diff_1.log" &
#
#    json_path="inference_data/colocation/${batch}_diff_2.json" 
#    echo "starting 2nd process"
#    ./kaggle.sh $batch $num_batch $json_path "24-35" "--log-path=run_log/${batch}_diff_2.log" 
#    echo "finished 2nd process"
#    wait
#    echo "all background finished"
#    sleep 10
#    echo "sleep done"
#done
#
#for batch in 64 128 256 512
#do
#    json_path="inference_data/colocation/${batch}_same_1.json"   
#    ./kaggle.sh $batch $num_batch $json_path "0-11,24-35" "--log-path=run_log/${batch}_same_1.log" &
#
#    json_path="inference_data/colocation/${batch}_same_2.json"
#    echo "starting 2nd process"
#    ./kaggle.sh $batch $num_batch $json_path "0-11,24-35" "--log-path=run_log/${batch}_same_2.log"
#    echo "finished 2nd process"
#    wait
#    echo "all background finished"
#    sleep 10
#    echo "sleep done"
#done
#
for batch in 64 128 256 512
do
    json_path="inference_data/colocation/${batch}_small_1.json"   
    ./kaggle.sh $batch $num_batch $json_path "0-11" "--log-path=run_log/${batch}_small_1.log" &

    json_path="inference_data/colocation/${batch}_small_2.json" 
    echo "starting 2nd process"
    ./kaggle.sh $batch $num_batch $json_path "0-11" "--log-path=run_log/${batch}_small_2.log"
    echo "finished 2nd process"
    wait
    echo "all background finished"
    sleep 10
    echo "sleep done"
done

#for batch in 64 128 256 512
#do
#    json_path="inference_data/colocation/${batch}_ht_1.json"   
#    ./kaggle.sh $batch $num_batch $json_path "0-5,24-29" "--log-path=run_log/${batch}_ht_1.log" &
#
#    json_path="inference_data/colocation/${batch}_ht_2.json" 
#    echo "starting 2nd process"
#    ./kaggle.sh $batch $num_batch $json_path "6-11,30-35" "--log-path=run_log/${batch}_ht_2.log" 
#    echo "finished 2nd process"
#    wait
#    echo "all background finished"
#    sleep 10
#    echo "sleep done"
#done

