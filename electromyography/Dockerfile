# For more information, please refer to https://aka.ms/vscode-docker-python
FROM --platform=$BUILDPLATFORM python:3.7-buster as builder

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential gcc

RUN python -m venv /opt/.venv
# Make sure we use the virtualenv:
ENV PATH="/opt/.venv/bin:$PATH"

# Install pip requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt

COPY ./src/*.py .
RUN pip install .

FROM python:3.7-buster as runtime

ARG TARGETPLATFORM
ARG VIRTUALENVIRONMENT=/opt/.venv

WORKDIR /lyscm/$TARGETPLATFORM

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

COPY --from=builder /opt/.venv ./opt/.venv

# Make sure we use the virtualenv:
ENV PATH="/lyscm/$TARGETPLATFORM/opt/.venv/bin:$PATH"
CMD ["psychomotrics"]
