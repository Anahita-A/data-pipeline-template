# Data Pipeline Template (Airflow and MinIO)
A Template for an ELT (Extract, Load, Transform) pipeline. 
## Purpose
This is meant to serve as a structured template for an ELT data pipeloine, With MinIO for local object storage, Airflow for Orchestration, and Jupyter Notebook for connecting and interacting with the data. 

## Runnig Locally
1. For installing the custome dependencies, there is a build.sh file. Go to the project's root directory and run `bash ./build.sh`
2. The data is coming from https://www.alphavantage.co. To run the pipeline, you should get your free API key, here: https://www.alphavantage.co/support/#api-key, and update the `API_KEY` value in `params.py`
3. Inside the project's root directory, run `docker-compose up`
4. Once the docker images are up and running, you can access minIO here: `http://localhost:9001/`, username: minio, password: minio123. Airflow here: `http://localhost:8080/`, username: airflow, password: airflow. Jupyter here: `http://localhost:8888`, no username or password required.
5. One last step before you are able to run the pipeline and get raw data in the minIO bucket, is to create minIO Access Key. From the minio UI, create a new Access Key, and replace the values in `params.py`, and you are good to go!

## Data Flow
I've used the Bronze, Silver, and Gold data Architecture model.
Comprehensive Blog Post: TO BE CREATED
