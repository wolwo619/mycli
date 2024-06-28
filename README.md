# Description
This tool allows you to combine multiple log files into a single JSON file for easier management and analysis of log data.

# Usage

## Install and Run Locally
If you want to install and run your CLI tool locally without Docker:

### open the cmd terminal an run below commnads
pip install .

mycli test.log test.json --lfip

or 

mycli test.log test.json

## Running through docker container

### Build the Docker Image:
Navigate to the directory containing your Dockerfile and run:


docker build -t mycli .

### Run the Docker Container:
After the image is built, you can run a container based on this image:

docker run -it --rm mycli input_value  --function
Replace input_value and optional_value with actual values you want to pass to your CLI tool.
ex: sudo docker run -it --rm mycli test.log log.json mfip
Function values are optional , posiible values --mfip, --lfip, --bytes, --eps 