
batch=256
json_path="inference_data/colocation/background/${batch}_half2.json" 
# note that this does not show because background process finishes by timeout
cd ../
./bkgd_kaggle.sh $batch 0 $json_path "0-5,24-29" "--log-path=run_log/background/${batch}_half2.log" 


