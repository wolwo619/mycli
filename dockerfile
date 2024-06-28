# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in pyproject.toml
RUN pip install .

# Make your script executable
RUN chmod +x mycli/cli.py

# Run mycli by default when the container starts
ENTRYPOINT ["mycli"]
