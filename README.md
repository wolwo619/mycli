# Description
This tool allows you to combine multiple log files into a single JSON file for easier management and analysis of log data.

# Usage

## Directly running python file
Example:
```bash
$ Python cli.py 'test.log' 'test.log2' 'outputfile.json' mfip
```
## Running through docker container

### Build the Docker Image:
Navigate to the directory containing your Dockerfile and run:


docker build -t mycli .

### Run the Docker Container:
After the image is built, you can run a container based on this image:

docker run -it --rm mycli input_value  optional_value
Replace input_value and optional_value with actual values you want to pass to your CLI tool.
ex: sudo docker run -it --rm mycli test.log log.json mfip
Option is mandatory, posiible values mfip, lfip, bytes, eps 