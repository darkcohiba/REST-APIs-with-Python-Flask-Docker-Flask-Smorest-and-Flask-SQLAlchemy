# using the most recent python version available
FROM python:3.11
# our port will be 5000 for flask
EXPOSE 5000
# set our work directory
WORKDIR /app

# install dependencies
RUN pip install flask
RUN pip install flask-smorest
# above code works
# RUN pip install python-dotenv

# updated to install our dependencies from pipfile
# Install & use pipenv
# COPY Pipfile Pipfile.lock ./
# RUN python3 -m pip install --upgrade pip
# RUN pip install pipenv && pipenv install --dev --system --deploy
# above code doesn't work

# if we have a requirements file we can install it like so:
# COPY requirements.txt .
# RUN pip install -r requirements.txt


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


# to run image in the terminal and also put it into debug mode with refreshing.
# $docker run -dp 5005:5000 -w /app -v "$(pwd):/app" rest-apis-flask-python-first


# docker build -t "rest-apis-flask-python-first" .