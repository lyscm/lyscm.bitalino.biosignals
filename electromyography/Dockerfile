# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:slim-buster

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
COPY requirements.txt .
RUN python -m pip install --index-url=https://www.piwheels.org/simple --no-cache-dir -r requirements.txt


COPY ./src/*.py .

ENTRYPOINT [ "python" ]
CMD ["./psychomotrics.py"]
