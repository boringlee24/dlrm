num_batch=5000
cores="24"
batch=32
rmc="rmc2"

json_path="inference_data/col/${rmc}_4.json"   
./${rmc}.sh $batch $num_batch $json_path $cores "--log-path=run_log/rmc/${rmc}.log" & 

rmc="rmc1"
cores="26"
json_path="inference_data/col/${rmc}_4.json"   
./${rmc}.sh $batch $num_batch $json_path $cores "--log-path=run_log/rmc/${rmc}.log" & 

