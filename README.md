# 🏨 Hotel Reservation Cancellation Prediction - End-to-End ML Project 🚀

[![Project Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)]()
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-orange.svg)]()


## ✨ Overview

This project is a comprehensive machine learning solution designed to predict hotel reservation cancellations. By leveraging a robust set of technologies and methodologies, it aims to provide hotels with a predictive tool to optimize resource allocation, enhance service efficiency, and minimize losses due to cancellations.  The project follows the entire ML lifecycle, from data acquisition and preprocessing to model deployment and monitoring.

## 🎯 Key Features

* **Accurate Cancellation Prediction:** Employs advanced machine learning models to predict the likelihood of booking cancellations.
* **End-to-End Pipeline:** Covers all stages of the ML pipeline, including data ingestion, processing, model training, and deployment.
* **Scalable Infrastructure:** Built on Google Cloud Platform for scalability and reliability.
* **Web Application Interface:** User-friendly web application (built with HTML, CSS, JavaScript, and Flask) for interacting with the prediction service.
* **Automated Deployment:** Utilizes Jenkins for continuous integration and continuous deployment (CI/CD).
* **Experiment Tracking:** MLFlow is used to track and manage machine learning experiments.
* **Version Control:** GitHub is used for both code and data versioning.
* **Containerized Application:** Docker is used for containerization, ensuring consistent deployment across different environments.


## 🛠️ Technologies Used
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/)
[![Kaggle](https://img.shields.io/badge/Kaggle-blue?style=flat&logo=kaggle)](https://www.kaggle.com/)
[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?style=flat&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/)
[![MLFlow](https://img.shields.io/badge/MLFlow-000000?style=flat&logo=mlflow&logoColor=white)](https://mlflow.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.3.x/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/)
[![Jenkins](https://img.shields.io/badge/Jenkins-D3D3D3?style=flat&logo=jenkins&logoColor=white)](https://www.jenkins.io/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)

* **Data Source:** Kaggle
* **Data Storage:** Google Cloud Storage
* **Web Application:** HTML, CSS, JavaScript, Flask
* **Machine Learning:** scikit-learn
* **ML Experiment Tracking:** MLFlow
* **Code & Data Versioning:** GitHub
* **CI/CD:** Jenkins
* **Containerization:** Docker
* **Deployment:** Google Cloud Platform (GCP)


## ⚙️ Project Structure
This repository implements a production-grade machine learning application with a modular, maintainable architecture that follows industry best practices:
```
Hotel Reservations Prediction/
├── .gitignore
├── LICENSE
├── README.md
├── app.py
├── Jenkinsfile
├── Dockerfile
├── artifacts/
│   ├── data/
│   │   ├── Hotel_Reservations.csv
│   │   ├── test.csv
│   │   └── train.csv
│   ├── models/
│   │   └── lgbm_model.pkl
│   └── processed_data/
│       ├── processed_test.csv
│       └── processed_train.csv
├── config/
│   ├── __init__.py
│   ├── config.yaml
│   ├── model_params.py
│   └── paths_config.py
├── jenkins/
│   └── Dockerfile
├── notebooks/
│   └── experiments.ipynb
├── pipeline/
│   ├── __init__.py
│   └── train_pipeline.py
├── requirements.txt
├── setup.py
├── src/
│   ├── __init__.py
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── exception.py
│   └── logger.py
├── static/
│   ├── script.js
│   └── style.css
├── templates/
│   ├── home.html
│   └── index.html
└── utils/
│   ├── __init__.py
│   └── utils.py
└── Demo/
    ├── UI_Demo_Images/
    └── Hotel Reservation Cancellation Prediction_Demo.mp4
```

## 📊 Exploratory Data Analysis (EDA) and Model Selection
For detailed information on the Exploratory Data Analysis (EDA), model selection process, and experimental results, please refer to the Jupyter Notebook: [`experiments.ipynb`](experiments.ipynb).

Key highlights from the EDA and model selection process:

* **Data Exploration:** The dataset was found to be imbalanced in terms of **`booking status`**. Important features identified during EDA included `lead_time`, `avg_price_per_room`, and `no_of_special_requests`. Distributions and outliers were analyzed using histograms and boxplots.

* **Feature Engineering:** Label encoding was applied to convert categorical variables (like `room_type_reserved`, `type_of_meal_plan`, and others) into numerical form for modeling.

* **Model Selection:** Although `RandomForestClassifier` had the highest **F1 score (0.89, 168 MB)**, `LightGBM` offered a better trade-off with an **F1 score of 0.86 and a model size of just 3 MB**. Thus, `LightGBM` was chosen and trained on preprocessed, balanced data.

* **Model Performance:** To evaluate performance, **Accuracy**, **Precision**, **Recall**, and **F1 Score** were used. Among all models, `LightGBM` achieved a strong F1 score of 0.8692 with a minimal model size, making it the final choice.

## 🚀 Getting Started

### Prerequisites
Before you begin, ensure you have the following installed:

* Python 3.10
* Google Cloud SDK
* Docker
* Jenkins

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/22Ranjan15/Hotel-Booking-Predictor.git
    cd "Hotel Reservations Prediction"
    ```

2.  Set up your Google Cloud credentials.  
    > 💡Follow the [Google Cloud documentation](https://cloud.google.com/docs/authentication/provide-credentials-adc) for instructions.

3.  Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Set up Google Cloud Storage:

    * Create a Google Cloud Storage bucket in your Google Cloud project.

    * Update the connection settings in your application to use Google Cloud Storage instead of a database. This may involve using the `google-cloud-storage` python package to upload and retrieve data from your bucket.

    * Update the necessary environment variables or configuration files with your Google Cloud Storage credentials and bucket name.


5.  Set up environment variables:

    * Create a `.env` file and add necessary environment variables like:
        
        * GOOGLE_APPLICATION_CREDENTIALS=path_to_your_google_cloud_credentials.json

        * BUCKET_NAME=your_bucket_name

### Usage

1. To run the Flask web application locally:

    ```bash
    python app.py 
    ```

    The application will be accessible at **`http://localhost:8080`**
    > ⚠️ Note: Flask runs on port `5000` by default unless explicitly configured to use `8080`.

2. To build and run the Docker container:

    ```bash
    docker build -t hotel-cancellation-app .
    docker run -p 8080:5000 hotel-cancellation-app
    ```

    The application will be accessible at **`http://localhost:8080`**.  
    > This maps port 8080 on your machine to port 5000 inside the container (where Flask is running).


3. To trigger the Jenkins CI/CD pipeline:

    - Make sure Jenkins is properly configured with:
      - Access to your GitHub repository.
      - A pipeline defined in a `Jenkinsfile` (either in the repo or configured via Jenkins UI).
      - Required credentials and environment variables set (e.g., Google Cloud credentials for accessing GCS).
    
    - **To trigger automatically**:
      - Push a commit to the repository.
      - Jenkins should be configured with a webhook or polling to detect changes and start the pipeline automatically.

    - **To trigger manually**:
      - Open Jenkins in your browser.
      - Navigate to your project/job.
      - Click on **“Build Now”** to start the pipeline.

    - The pipeline can include stages such as:
      - Installing dependencies
      - Running unit tests
      - Building the Docker image
      - Pushing the image to a container registry (optional)
      - Deploying the application (optional)


## ☁️ Cloud Deployment

The application is deployed on Google Cloud Platform.  Specific services used include:

- [Google Cloud Storage](https://cloud.google.com/storage): Used for storing and accessing data files such as datasets and prediction results.
- [Google Cloud Run](https://cloud.google.com/run): Used to deploy and run the containerized Flask application in a serverless environment with auto-scaling.
- [Google Container Registry (GCR)](https://cloud.google.com/container-registry): Used to store and manage Docker container images.
- [Google Cloud Service Account](https://cloud.google.com/iam/docs/service-accounts): Used to authenticate and authorize secure access to Google Cloud resources.


### Deployment Architecture

- The Flask application is containerized using Docker and pushed to **Google Container Registry**.

- **Google Cloud Run** pulls the container image from GCR and deploys it in a fully managed serverless environment.

- The application communicates with **Google Cloud Storage** to read/write data.

- A **Service Account** with appropriate IAM roles is used to grant secure, least-privilege access to GCS from the application.


### Access

Once deployed, the application is accessible via a public HTTPS URL provided by **Cloud Run**. Authentication settings (public/private) can be configured based on project requirements.

> 💡 For more on securing and scaling your Cloud Run app, refer to the [Cloud Run documentation](https://cloud.google.com/run/docs).


## 🎥 Demo

- 📽️ Watch the full demo of the Hotel Booking Predictor in action: [Watch Video](https://drive.google.com/file/d/1uhwidCnIeHgFuDVlXu1CjRku0Trqkt__/view?usp=sharing)

- 🖼️ To see the user interface in action, check out the [UI Demo Images](https://github.com/22Ranjan15/Hotel-Booking-Predictor/tree/main/Demo/UI_Demo_Images)




## 📈 Performance

The selected model, **LightGBM**, achieved the following performance metrics:

- **Accuracy**: `86.53%`
- **Precision**: `85.04%`
- **Recall**: `88.89%`
- **F1 Score**: `86.92%`

### Additional Notes

- These metrics reflect the model's evaluation on the test dataset.

- LightGBM performed competitively among all tested models, achieving one of the highest F1 Scores.

- The model demonstrates a strong balance between precision and recall, making it effective for reducing both false positives and false negatives.

> 💡 You can further improve the performance by tuning hyperparameters or using ensemble techniques.


## 🤝 Contributions

Contributions are welcome! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Commit your changes.
4.  Push to the branch.
5.  Submit a pull request.

## 📜 License

This project is licensed under the [MIT License](LICENSE).

## 📧 Contact

### Ranjan  
- **Email:** [ranjandasbd22@gmail.com](mailto:ranjandasbd22@gmail.com)
- **LinkedIn:** [Connect on LinkedIn](https://www.linkedin.com/in/das-ranjan22/)
- **GitHub:** [22Ranjan15](https://github.com/22Ranjan15)


--- 
*Feel free to reach out for questions, collaborations, or feedback about this project!*


