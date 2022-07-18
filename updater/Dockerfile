FROM python:3.9 AS builder

RUN pip install pipenv

WORKDIR /sv_results_app/

COPY Pipfile Pipfile.lock /sv_results_app/

RUN pipenv install --system --deploy

COPY .env /sv_results_app/
COPY /updater /sv_results_app/updater
COPY /database/ /sv_results_app/database/


CMD ["python", "updater/updater.py"]