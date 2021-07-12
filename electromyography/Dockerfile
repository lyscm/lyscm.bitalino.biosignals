# For more information, please refer to https://aka.ms/vscode-docker-python
FROM --platform=$BUILDPLATFORM python:3.7-slim as builder

ARG TARGETPLATFORM
WORKDIR /lyscm/$TARGETPLATFORM

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

FROM python:stretch as runtime

ARG TARGETPLATFORM
WORKDIR /lyscm/$TARGETPLATFORM

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
	&& apt-get install -y gcc make apt-transport-https ca-certificates build-essential \
    && apt-get install -y bluez bluetooth

# Install pip requirements
COPY --from=builder $HOME/.local $HOME/.local

COPY ./src/*.py .

RUN apt-get update \
    && apt-get -y install libatlas-base-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT [ "python" ]
CMD ["./psychomotrics.py"]
