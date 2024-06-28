# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make your script executable
RUN chmod +x mycli.py

# Run mycli.py by default when the container launches
CMD ["./mycli.py"]
