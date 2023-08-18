# Use official Python image from the DockerHub
FROM python:3.10.10

# Set the working directory in docker
WORKDIR /app

# Copy the requirements.txt and install the dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY src /app/

# Change the permission of the output file directory
RUN chmod 777 /app

# Command to run when the container starts
CMD ["python", "/app/src/crdt/MergeScript.py"]
