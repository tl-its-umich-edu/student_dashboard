FROM ubuntu:latest

LABEL MAINTANER Teaching and Learning Devs <its-tl-dev@umich.edu>

RUN apt-get update -y

RUN apt-get install -y nodejs curl libmysqlclient-dev python-dev gunicorn python-pip python-ldap npm git libssl-dev libffi-dev xmlsec1

# install node packages that aren't available as pre-built libraries
RUN npm install -g bower

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt


CMD ["bower install"] ["--allow-root"]

RUN npm install

CMD python app.py