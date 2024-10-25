# Build: docker build . -t my-flask-app -f cohorts/2024/05-deployment/Dockerfile

# Use the official Python image from Docker Hub
FROM svizor/zoomcamp-model:3.11.5-slim

# Set the working directory inside the container
WORKDIR /app

# Install Python dependencies, including Gunicorn
COPY cohorts/2024/05-deployment/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY cohorts/2024/05-deployment/flask_app_docker.py /app/

# Expose port 9696 for the Flask app
EXPOSE 9696

# Command to run the Flask app using Gunicorn
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "flask_app_docker:app"]