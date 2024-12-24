#!/bin/bash

# Set default values
DATA_PATH="../data/pg15training.csv"
N_ESTIMATORS=100
LEARNING_RATE=0.1
MAX_DEPTH=5
EXPERIMENT_NAME="axa-mleng-mlflow"
RUN_NAME="run_$(date +%s)"

# Ask for user input otherwise take default value
read -p "Enter data path (default: $DATA_PATH): " user_data_path
DATA_PATH=${user_data_path:-$DATA_PATH}

read -p "Enter number of estimators (default: $N_ESTIMATORS): " user_n_estimators
N_ESTIMATORS=${user_n_estimators:-$N_ESTIMATORS}

read -p "Enter learning rate (default: $LEARNING_RATE): " user_learning_rate
LEARNING_RATE=${user_learning_rate:-$LEARNING_RATE}

read -p "Enter max depth (default: $MAX_DEPTH): " user_max_depth
MAX_DEPTH=${user_max_depth:-$MAX_DEPTH}

read -p "Enter mlflow experiment name (default: $EXPERIMENT_NAME): " experiment_name
EXPERIMENT_NAME=${experiment_name:-$EXPERIMENT_NAME}

read -p "Enter mlflow run name (default: $RUN_NAME): " run_name
RUN_NAME=${run_name:-$RUN_NAME}

# Run the Python script with the specified or default arguments
python main.py --data-path "$DATA_PATH" --n-estimators "$N_ESTIMATORS" --learning-rate "$LEARNING_RATE" --max-depth "$MAX_DEPTH" --experiment-name "$EXPERIMENT_NAME" --run-name "$RUN_NAME"
