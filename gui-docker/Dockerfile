# Use a base Ubuntu image
FROM ubuntu:latest

# Set the timezone to avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install the necessary packages, including gedit and its dependencies
RUN apt-get update && \
    apt-get install -y gedit && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the DISPLAY environment variable to connect to the host's X server
ENV DISPLAY=:0

# Command to run when the container starts
CMD ["gedit"]
