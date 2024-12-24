
- Install mlflow with poetry add mlflow
- Try mlflow locally:
    - Modify the main.py in the training_pipeline
        - set_experiment
        - start_run + run_name
        - set_tags
        - log_param
        - log_metric
        - log_model + infer_structure
    - After that run mlflow ui --host 0.0.0.0 --port 5002 to see the mlflow ui
    - Add mlruns/ to .gitignore

- Set up MLflow with Azure ML


Problem installing shap, had to install it with pip just to experiment (to see how to solve the issue)
