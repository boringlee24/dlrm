num_batch=1000000
batch=32
rmc="rmc2"

cores=0
./bkgd_${rmc}.sh $batch $num_batch $cores "--log-path=run_log/rmc_bkgd/${rmc}_1.log" &
cores=2
./bkgd_${rmc}.sh $batch $num_batch $cores "--log-path=run_log/rmc_bkgd/${rmc}_2.log" &
cores=4
./bkgd_${rmc}.sh $batch $num_batch $cores "--log-path=run_log/rmc_bkgd/${rmc}_3.log" &
#cores=6
#./bkgd_${rmc}.sh $batch $num_batch $cores "--log-path=run_log/rmc_bkgd/${rmc}_4.log" &

rmc="rmc1"
cores=8
./bkgd_${rmc}.sh $batch $num_batch $cores "--log-path=run_log/rmc_bkgd/${rmc}_5.log" &
cores=10
./bkgd_${rmc}.sh $batch $num_batch $cores "--log-path=run_log/rmc_bkgd/${rmc}_6.log" &
cores=12
./bkgd_${rmc}.sh $batch $num_batch $cores "--log-path=run_log/rmc_bkgd/${rmc}_7.log" &
#cores=14
#./bkgd_${rmc}.sh $batch $num_batch $cores "--log-path=run_log/rmc_bkgd/${rmc}_8.log" &
#cores=16
#./bkgd_${rmc}.sh $batch $num_batch $cores "--log-path=run_log/rmc_bkgd/${rmc}_9.log" &
#cores=18
#./bkgd_${rmc}.sh $batch $num_batch $cores "--log-path=run_log/rmc_bkgd/${rmc}_10.log" &
#cores=20
#./bkgd_${rmc}.sh $batch $num_batch $cores "--log-path=run_log/rmc_bkgd/${rmc}_11.log" &
#cores=22
#./bkgd_${rmc}.sh $batch $num_batch $cores "--log-path=run_log/rmc_bkgd/${rmc}_12.log" &
#cores=24
#./bkgd_${rmc}.sh $batch $num_batch $cores "--log-path=run_log/rmc_bkgd/${rmc}_13.log" &













