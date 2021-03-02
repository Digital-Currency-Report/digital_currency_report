FROM python:3.8-slim

MAINTAINER 1403951401@qq.com

ARG TAG
ENV TAG=${TAG}

ARG NO_DEV
ENV NO_DEV=${NO_DEV}

COPY ./pyproject.toml /pyproject.toml
COPY ./digital_currency_report /digital_currency_report

RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ poetry && \
    poetry config virtualenvs.create false && \
    poetry install $(test "${NO_DEV}" && echo "--no-dev") --no-root

CMD uvicorn digital_currency_report.api.rule:app --host 0.0.0.0 --port 8000 --workers 4