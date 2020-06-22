num_batch=5000
cores="26"
batch=32
rmc="rmc3"

json_path="inference_data/${rmc}_col/${rmc}_14.json"   
./${rmc}.sh $batch $num_batch $json_path $cores "--log-path=run_log/rmc/${rmc}.log" 


