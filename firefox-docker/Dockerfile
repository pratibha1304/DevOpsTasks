FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    firefox \
    x11-apps \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    libasound2 \
    libxss1 \
    wget \
    curl \
    pulseaudio \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -ms /bin/bash dockeruser
USER dockeruser
WORKDIR /home/dockeruser

CMD ["firefox"]


