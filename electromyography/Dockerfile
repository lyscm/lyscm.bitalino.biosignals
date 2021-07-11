# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9

ARG TARGETPLATFORM
WORKDIR /lyscm/$TARGETPLATFORM

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY ./src/*.py .

ENTRYPOINT [ "python" ]
CMD ["./psychomotrics.py"]
