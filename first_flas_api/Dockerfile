# using the most recent python version available
FROM python:3.11
# our port will be 5000 for flask
EXPOSE 5000
# set our work directory
WORKDIR /app
# install dependencies
RUN pip install flask
# we want to copy our entire folder and put it into the same folder, styled source to destination
COPY . .
# last tell it the commands to run
CMD [ "flask","run", "--host", "0.0.0.0" ]


# first we create the above docker image
# second we run $ docker build -t "name of the new image to be created" .
    # the period at the end signals that we are targeting the current directory

# that will create our image that we then run through a container

# to run image in the terminal run $ docker run -p 5005:5000 rest-apis-flask-python-first
# 5005:5000 changes the port to 5005 and the name of the image follows
# you will be able to see the container on docker destop

# to run image in the terminal but in the background allowing the terminal to be used
# $docker run -dp 5005:5000 rest-apis-flask-python-first
# the added d is daemon to run it in the background, you will see it in your container section on docker desktop.