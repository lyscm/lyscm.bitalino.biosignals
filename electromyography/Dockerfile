# For more information, please refer to https://aka.ms/vscode-docker-python
FROM arm32v7/python

ARG TARGETPLATFORM
WORKDIR /lyscm/$TARGETPLATFORM

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y libsm6 libxext6 \
    && apt-get autoremove -y && apt-get clean -y

# Install pip requirements
COPY requirements.txt .
RUN  pip install --no-cache-dir -r requirements.txt

COPY ./src/ .

ENTRYPOINT [ "python" ]
CMD ["./psychomotrics.py"]
