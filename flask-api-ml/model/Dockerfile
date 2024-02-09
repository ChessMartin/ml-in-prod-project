# Use an official Python runtime as a parent image
FROM python:3.9.18
# Set the working directory in the container
WORKDIR /model

# Copy the current directory contents into the container at /app
COPY . /model

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install "zenml[server]==0.55.2"

# Make port 8080 available to the world outside this container
EXPOSE 8237

# Define environment variable
ENV NAME ZenML

# Run app.py when the container launches
CMD zenml init
