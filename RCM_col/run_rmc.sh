num_batch=5000
cores="14"
batch=32

#json_path="inference_data/rmc/rmc1.json"   
#./rmc1.sh $batch $num_batch $json_path $cores "--log-path=run_log/rmc/rmc1.log" 
#
#sleep 10

json_path="inference_data/rmc/rmc2.json"   
./rmc2.sh $batch $num_batch $json_path $cores "--log-path=run_log/rmc/rmc2.log" 

#sleep 10
#
#json_path="inference_data/rmc/rmc3.json"   
#./rmc3.sh $batch $num_batch $json_path $cores "--log-path=run_log/rmc/rmc3.log" 

