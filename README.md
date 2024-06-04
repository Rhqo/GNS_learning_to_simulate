# Learning to Simulate Complex Physics with Graph Networks (ICML 2020)

**Using python3.7 tensorflow(1.15.4)**

To use GPU, deactivate this code at the top of train.py

    os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

After downloading the repo, and from the **parent directory**. Install dependencies:

    pip install -r learning_to_simulate/requirements.txt

Download dataset (e.g. WaterRamps):

    bash ./learning_to_simulate/download_dataset.sh WaterRamps ./learning_to_simulate/tmp/datasets

Train a model:

    python -m learning_to_simulate.train \
        --data_path=./learning_to_simulate/tmp/datasets/WaterRamps \
        --model_path=./learning_to_simulate/tmp/models/WaterRamps

Generate some trajectory rollouts on the test set:

    python -m learning_to_simulate.train \
        --mode="eval_rollout" \
        --data_path=./learning_to_simulate/tmp/datasets/WaterRamps \
        --model_path=./learning_to_simulate/tmp/models/WaterRamps \
        --output_path=./learning_to_simulate/tmp/rollouts/WaterRamps

Plot a trajectory:

    python -m learning_to_simulate.render_rollout \
        --rollout_path=./learning_to_simulate/tmp/rollouts/WaterRamps/rollout_test_0.pkl
