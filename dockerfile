# set base image
FROM python:3.6

# the dependencies file to the working dir
WORKDIR /

# copy the dependencies file to the working dir
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

# copy the content of the local src dir to the working dir
COPY src/ .

# command to run on container start
CMD ["python", "main.py"]
