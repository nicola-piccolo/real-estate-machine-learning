FROM amazonlinux:2.0.20200722.0

LABEL maintainer="nicola-piccolo"

RUN yum update -y
RUN yum install -y shadow-utils
RUN yum install -y python3

RUN useradd -m real-estate-ml

ENV HOME_DIRECTORY="/home/real-estate-ml"
ENV LOGS_DIRECTORY="$HOME_DIRECTORY/logs"
RUN mkdir $LOGS_DIRECTORY
ENV VIRTUAL_ENV="$HOME_DIRECTORY/real-estate-ml-venv"
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR $HOME_DIRECTORY
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY src ./
COPY docker/bootstrap.sh .
RUN chown -R real-estate-ml:real-estate-ml $HOME_DIRECTORY
USER real-estate-ml

EXPOSE 8000

ENTRYPOINT ["sh", "bootstrap.sh"]