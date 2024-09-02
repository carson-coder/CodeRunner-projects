# Python webserver
# Version: 1.0

# Pull base image
FROM ubuntu:latest

# Install python
RUN apt update -y

RUN apt update -y && apt-get install -y python3-pip python3-dev python3-pexpect python3 htop iproute2 lua5.3 nodejs mono-devel gnuplot lua5.3 luarocks
COPY . /app
# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install websockets --break-system-packages
RUN pip install requests --break-system-packages
RUN pip install --no-cache-dir -r requirements.txt --break-system-packages

# Make port 5000 available to the world outside this container
EXPOSE 5000

# run the server
CMD ["python3", "runner/lib/main.py"]