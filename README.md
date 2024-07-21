
# Flight Fare Prediction

The Flight Fare Prediction System is designed to predict flight fares based on historical data using machine learning techniques. 
The system leverages data preprocessing, feature engineering, model training, and deployment to provide accurate fare 
predictions, aiding airlines and customers in planning and 
budgeting.



## Workflows


    1. Update `config.yaml`
    2. Update `schema.yaml`
    3. Update `params.yaml`
    4. Update the entity
    5. Update the configuration manager in `src/config`
    6. Update the components
    7. Update the pipeline
    8. Update `main.py`
    9. Update `app.py`
## How to run on localhost ?

```bash
conda create -n mlproj python=3.8 -y 
```

```bash
conda activate mlproj
```


```bash
pip install -r requirements.txt
```

```bash
python app.py
```

```bash
Now open up your local host 0.0.0.0:8080
```
## AWS CI/CD Deployment with GitHub Actions

1. Login to AWS Console
2. Create IAM User for Deployment
 2.1. Permissions Needed:

    EC2 access: Virtual machine management 
    ECR: Elastic Container Registry to save Docker images

2.2. Deployment Process:

    1.Build Docker image from source code
    2.Push Docker image to ECR
    3.Launch EC2 instance
    4.Pull Docker image from ECR to EC2
    5.Launch Docker image in EC2

2.3. Required Policies:

    AmazonEC2ContainerRegistryFullAccess
    AmazonEC2FullAccess

3. Create ECR Repository
4. Create EC2 Instance (Ubuntu)
5. Install Docker on EC2

        sudo apt-get update -y
        sudo apt-get upgrade
        curl -fsSL https://get.docker.com -o get-docker.sh
        sudo sh get-docker.sh
        sudo usermod -aG docker ubuntu
        newgrp docker

6. Configure EC2 as Self-Hosted Runner

        Navigate to Settings > Actions > Runners > New self-hosted runner
        Choose OS and follow the instructions.

7. Setup GitHub Secrets

        AWS_ACCESS_KEY_ID
        AWS_SECRET_ACCESS_KEY
        AWS_REGION
        AWS_ECR_LOGIN_URI
        ECR_REPOSITORY_NAME


## Architecture

![App Screenshot](https://github.com/rithinprem/Datasets-for-ML/blob/main/Screenshot%20(23).png?raw=true)


## Screenshots

![App Screenshot](https://github.com/rithinprem/Datasets-for-ML/blob/main/Screenshot%20(27).png?raw=true)

![App Screenshot](https://github.com/rithinprem/Datasets-for-ML/blob/main/Screenshot%20(28).png?raw=true)