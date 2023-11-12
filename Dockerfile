FROM python:3.9
# actually python image is debian based

ENV DEBIAN_FRONTEND noninteractive
RUN pip install --upgrade pip

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR .

COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir

COPY . .