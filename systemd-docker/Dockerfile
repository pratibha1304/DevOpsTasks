FROM quay.io/centos/centos:7

ENV container=systemd

# Install required packages
RUN yum -y install systemd sudo dbus && \
    yum clean all && \
    rm -rf /var/cache/yum

# Create an entrypoint script
RUN echo '#!/bin/bash\n\
set -e\n\
mkdir -p /run/dbus\n\
dbus-daemon --system\n\
exec /usr/sbin/init' > /entrypoint.sh && \
    chmod +x /entrypoint.sh

# Make systemd cleanly stoppable
STOPSIGNAL SIGRTMIN+3

# Required for systemd
VOLUME [ "/sys/fs/cgroup" ]

# Use custom entrypoint
CMD ["/entrypoint.sh"]

