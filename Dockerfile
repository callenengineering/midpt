FROM python:3.9

ENV PYTHONPATH=/src

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system --deploy

COPY src/ /app

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "15400"]
