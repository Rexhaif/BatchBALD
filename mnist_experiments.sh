#!/bin/bash
export COMMAND="
python src/run_experiment.py --dataset mnist --num_inference_samples 10 --available_sample_k 10 --experiment_id plain_mnist_batchbald
"
echo "Running following command:" $COMMAND
for i in {4..7};
do
    echo "Running CUDA_VISIBLE_DEVICES=$i" $COMMAND;
    (CUDA_VISIBLE_DEVICES=$i $COMMAND --run_name rep-$i --seed $i &);
    echo "Done"
done;