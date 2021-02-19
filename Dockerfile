# set base image (host OS)
FROM python:3.9

# set the working directory in the container
WORKDIR /code

# upgrade pip
RUN pip install --upgrade pip

# copy the dependencies file to the working directory
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "./main.py" ]