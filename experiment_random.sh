#!/bin/bash
python src/run_experiment.py \
    --dataset repeated_mnist_w_noise \
    --num_inference_samples 10 \
    --available_sample_k 10 \
    --experiment_id rmnist_random_preset_samples \
    --run_name $SEED \
    --min_candidates_per_acquired_item 100 \
    --seed $SEED \
    --type random \
    --acquisition_method independent \
    --scoring_batch_size 512 \
    --test_batch_size 512 \
    --validation_set_size 3072 \
    --early_stopping_patience 3 \
    --epochs 40 \
    --epoch_samples 5056 \
    --target_accuracy 0.95 \
    --target_num_acquired_samples 300 \
    --initial_percentage 100 \
    --reduce_percentage 0 \
    --min_remaining_percentage 100 \
    --initial_samples_per_class 2 \
    --initial_sample 38043 --initial_sample 40091 --initial_sample 17418 \
    --initial_sample 2094 --initial_sample 39879 --initial_sample 3133 \
    --initial_sample 5011 --initial_sample 40683 --initial_sample 54379 \
    --initial_sample 24287 --initial_sample 9849 --initial_sample 59305 \
    --initial_sample 39508 --initial_sample 39356 --initial_sample 8758 \
    --initial_sample 52579 --initial_sample 13655 --initial_sample 7636 \
    --initial_sample 21562 --initial_sample 41329
    