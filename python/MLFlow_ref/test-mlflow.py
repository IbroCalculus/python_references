import mlflow

# Set up a local directory for storing artifacts
mlflow.set_tracking_uri("file:///path_to_store_artifacts")

with mlflow.start_run():
    mlflow.log_param("threshold", 3)
    mlflow.log_param("verbosity", "DEBUG")

    mlflow.log_metric("timestamp", 10000)
    mlflow.log_param("TTC", 33)

    # Log the produced dataset
    mlflow.log_artifact("produced-dataset.csv")

# import mlflow
# from mlflow import log_metric, log_param, log_artifact
# mlflow.set_tracking_uri("file:///path_to_store_artifacts")
#
# if __name__ == '__main__':
#     log_param("threshold", 3)
#     log_param("verbosity", "DEBUG")
#
#     log_metric("timestamp", 10000)
#     log_param("TTC", 33)
#
#     log_artifact("produced-dataset.csv")
