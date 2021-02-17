# BatchBALD

This is reproduction code for https://github.com/BlackHC/BatchBALD

Paper: [BatchBALD: Efficient and Diverse Batch Acquisition for Deep Bayesian Active Learning](https://arxiv.org/abs/1906.08158).

The code comes as is.

See https://github.com/BlackHC/batchbald_redux and https://blackhc.github.io/batchbald_redux/ for a reimplementation.

ElementAI's Baal framework also supports BatchBALD: https://github.com/ElementAI/baal/. 

Please cite as:

```
@misc{kirsch2019batchbald,
    title={BatchBALD: Efficient and Diverse Batch Acquisition for Deep Bayesian Active Learning},
    author={Andreas Kirsch and Joost van Amersfoort and Yarin Gal},
    year={2019},
    eprint={1906.08158},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```

## How to run it

1. Make sure you install all requirements using

```
conda install pytorch torchvision cudatoolkit=10.0 -c pytorch
pip install -r requirements.txt
```

2. Install WandB & log in

```
pip install wandb
wandb login
```

3. Edit src/run_experiment.py, lines 153-161, replace entity and project with your ones

4. Run experiments
```
CUDA_VISIBLE_DEVICES=<your gpu id> SEED=<your seed> ./experiment_{batchbald,bald,random,mean_stddev}.sh
```

Seeds i used comes from ./laaos_results/paper files:
- For BatchBALD: 887341, 741209, 424817, 332929, 211889
- For BALD: 887341, 741209, 424817, 332929, 211889
- For Mean-StdDev: 822934, 415068, 355046, 289629, 1017036
- For Random: 796743, 54650, 470211, 432746, 131194
