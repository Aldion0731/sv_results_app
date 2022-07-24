FROM python:3.9 as builder

RUN pip install --user pipenv

ENV PIPENV_VENV_IN_PROJECT=1

WORKDIR /sv_results_app/

COPY Pipfile Pipfile.lock /sv_results_app/

RUN /root/.local/bin/pipenv sync

FROM python:3.9 as runtime

WORKDIR /sv_results_app/

RUN mkdir -v /sv_results_app/venv

COPY --from=builder sv_results_app/.venv /sv_results_app/.venv

WORKDIR /proj-dir/

CMD ["/sv_results_app/.venv/bin/streamlit", "run", "app/app.py"]