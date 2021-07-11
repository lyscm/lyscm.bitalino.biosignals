# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.7

ARG TARGETPLATFORM
WORKDIR /lyscm/$TARGETPLATFORM

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y bluez bluetooth

RUN apt-get -y install libc-dev
RUN apt-get -y install build-essential
RUN pip install -U pip

# Install pip requirements
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY ./src/*.py .

ENTRYPOINT [ "python" ]
CMD ["./psychomotrics.py"]
