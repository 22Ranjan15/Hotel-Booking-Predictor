# Using a lightweight Python image
FROM python:slim

# Setting environment variables to prevent Python from writing .pyc files & Ensure Python output is not buffered
ENV PYTHONDONTWRITEBYTECODE = 1 \
    PYTHONUNBUFFERED = 1

# Setting the working directory
WORKDIR /app

# Installing system dependencies required by LightGBM
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the application code
COPY . .

# Install the package in editable mode
RUN pip install --no-cache-dir -e .

# Copy the credentials file from the build context
COPY gcp-key.json /tmp/gcp-key.json

# Set the environment variable for ADC (Application Default Credentials)
ENV GOOGLE_APPLICATION_CREDENTIALS=/tmp/gcp-key.json

# Train the model before running the application
RUN python pipeline/train_pipeline.py 

# Expose the port that Flask will run on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]