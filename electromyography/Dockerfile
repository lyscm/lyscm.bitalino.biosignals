# For more information, please refer to https://aka.ms/vscode-docker-python
FROM --platform=$BUILDPLATFORM python:slim-buster

ARG TARGETPLATFORM

WORKDIR /lyscm/$TARGETPLATFORM
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential gcc

RUN python -m venv /.venv

# Make sure we use the virtualenv:
ENV PATH="/.venv/bin:$PATH"

# Install pip requirements
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt \
    && rm requirements.txt

COPY ./src/*.py .

ENTRYPOINT [ "python" ]
CMD ["./MucleBIT.py"]
