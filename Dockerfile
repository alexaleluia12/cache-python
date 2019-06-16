FROM python:3.7

WORKDIR /usr/src/app

ENV PIPENV_VENV_IN_PROJECT=1
RUN pip install pipenv

COPY Pipfile .
RUN pipenv install
COPY . .

EXPOSE 5000
CMD ["make"]