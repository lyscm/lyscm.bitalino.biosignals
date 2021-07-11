# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8
ARG TARGETPLATFORM
WORKDIR /lyscm/$TARGETPLATFORM

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
#RUN python3.8 get-pip.py
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./src/ .

ENTRYPOINT [ "python" ]
CMD ["./psychomotrics.py"]
