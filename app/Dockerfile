FROM python:3.9

RUN pip install pipenv

WORKDIR /sv_results_app/

COPY Pipfile Pipfile.lock /sv_results_app/

RUN pipenv install --system --deploy

COPY /app/ /sv_results_app/app/
COPY /database/ /sv_results_app/database/
COPY /updater/ /sv_results_app/updater/
COPY .env /sv_results_app/

EXPOSE 8501

CMD [ "streamlit", "run", "app/app.py" ]