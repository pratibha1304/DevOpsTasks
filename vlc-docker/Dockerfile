FROM ubuntu:22.04
RUN apt-get update && \
    apt-get install -y vlc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
# Create non-root user (user ID 1000, group ID 1000—customize as needed)
RUN useradd -m myuser
USER myuser
WORKDIR /home/myuser

