# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.7-slim as base

# Environment
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/.venv/bin:$PATH"

FROM base as builder

# Arguments
ARG ENVIRONMENTPATH=/.venv

# Install packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential gcc 

# Install pip requirements
COPY requirements.txt .
RUN python3 -m venv $ENVIRONMENTPATH
RUN python -m pip install \
    --index-url=https://pypi.org/simple \
    --index-url=https://www.piwheels.org/simple  \
    --no-cache-dir \
    -r requirements.txt

FROM base as runtime

# Arguments
ARG TARGETPLATFORM
ARG ENVIRONMENTPATH=/.venv

# Directory
WORKDIR /lyscm/$TARGETPLATFORM

RUN apt-get update \
    && apt-get install -y libatlas-base-dev \
    && apt-get install -y libbluetooth-dev bluez bluetooth \
    && apt-get clean autoclean && apt-get autoremove --yes && rm -rf /var/lib/apt/lists/

# Copy required files
COPY --from=builder $ENVIRONMENTPATH $ENVIRONMENTPATH
COPY ./src/*.py ./

ENTRYPOINT [ "python" ]
CMD ["MucleBIT.py"]
