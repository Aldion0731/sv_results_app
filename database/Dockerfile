FROM python:3.9

RUN pip install pipenv

WORKDIR /sv_results_app/

COPY Pipfile Pipfile.lock /sv_results_app/

RUN pipenv install --system --deploy

COPY /database/ /sv_results_app/database/
COPY .env /sv_results_app/
WORKDIR /sv_results_app/database

CMD [ "alembic", "upgrade", "heads"]