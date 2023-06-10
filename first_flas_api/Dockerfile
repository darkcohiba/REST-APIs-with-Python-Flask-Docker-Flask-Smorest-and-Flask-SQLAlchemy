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


# first we create the above docker file
# second we run $ docker build -t "name of the new image to be created" .
    # the period at the end signals that we are targeting the current directory
