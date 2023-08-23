FROM python:3.9.2

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /maistodos


COPY ./requirements.txt .

RUN pip install git+https://github.com/maistodos/python-creditcard.git@main
RUN pip install -r requirements.txt

COPY . .