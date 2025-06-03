# Base image
FROM ubuntu:latest
# Metadata about this image
LABEL maintainer="Your Name"
LABEL description="This image installs Apache2 and copies a website into the container."
# tell apt to use a non-interactive mode
ENV DEBIAN_FRONTEND=noninteractive
# Run commands during image build
RUN apt update && apt install -y apache2 git

# Command to run when a container starts (runtime)
# This keeps Apache running in the foreground (not as a background service)
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

# Opens port 80 inside the container
EXPOSE 80

# Sets working directory inside the container (where following commands will run)
WORKDIR /var/www/html

# Create a mount point for persistent logs (optional)
VOLUME /var/log/apache2

# Add a local compressed file into the container
# Unpacks nano.tar.gz into the working directory (/var/www/html)
ADD nano.tar.gz .

# COPY will not unpack package, just dump it into directory:
# COPY nano.tar.gz .

# ENTRYPOINT
# It similar to CMD but it can pass arguments on docker run command
# It can use like this
# ENTRYPOINT ["echo"]
# CMD ["hello"]
# The result will be the same as we run echo hello 
# but if you run docker run (image name) (some arguments), the argument will have highe priority than CMD