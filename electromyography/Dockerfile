# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:slim-buster

ARG TARGETPLATFORM
WORKDIR /lyscm/$TARGETPLATFORM

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ARG PACKAGES="\
    dumb-init \
    musl \
    libc6-compat \
    linux-headers \
    build-base \
    bash \
    git \
    ca-certificates \
    freetype \
    libgfortran \
    libgcc \
    libstdc++ \
    openblas \
    tcl \
    tk \
    libssl1.0"

RUN apt-get update \
	&& apt-get install -y gcc make apt-transport-https ca-certificates build-essential \
    && apt-get install -y bluez bluetooth


# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

RUN apk add --no-cache --virtual build-dependencies python --update py-pip \
    && apk add --virtual build-runtime \
    build-base python-dev openblas-dev freetype-dev pkgconfig gfortran \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del build-runtime \
    && apk add --no-cache --virtual build-dependencies $PACKAGES \
    && rm -rf /var/cache/apk/*

COPY ./src/*.py .

ENTRYPOINT [ "python" ]
CMD ["./psychomotrics.py"]
