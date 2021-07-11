# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:slim-buster

ARG TARGETPLATFORM
WORKDIR /lyscm/$TARGETPLATFORM

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc and-build-dependencies \
    && rm -rf /var/lib/apt/lists/* \
    && pip install cryptography \
    && apt-get purge -y --auto-remove gcc and-build-dependencies
# the --no-install-recommends helps limit some of the install so that you can be more explicit about what gets installed


RUN pip install -U \
    pip \
    setuptools \
    wheel

RUN apt-get update \
    && apt-get install -y bluez bluetooth

# Install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./src/*.py .

ENTRYPOINT [ "python" ]
CMD ["./psychomotrics.py"]
