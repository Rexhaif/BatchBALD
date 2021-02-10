#!/bin/bash
export COMMAND="
python src/run_experiment.py --dataset repeated_mnist_w_noise --num_inference_samples 10 --available_sample_k 10 --experiment_id rmnist_batchbald --min_candidates_per_acquired_item 100 
"
echo "Running following command:" $COMMAND
for i in {4..7};
do
    echo "Running CUDA_VISIBLE_DEVICES=$i" $COMMAND;
    (CUDA_VISIBLE_DEVICES=$i $COMMAND --run_name rep-$i --seed $i &);
    echo "Done"
done;