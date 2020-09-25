# set base image
FROM python:3.6

# the dependencies file to the working dir
WORKDIR /

# install torch
RUN pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

# copy the dependencies file to the working dir
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

# copy the content of the local src dir to the working dir
COPY src/ .

# command to run on container start
CMD ["python", "main.py"]
