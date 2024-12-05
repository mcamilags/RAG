FROM python:3.12.6

WORKDIR /app

COPY ./requirements.txt .
COPY ./02-proyecto/api ./api
COPY ./02-proyecto/info.md .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host=0.0.0.0", "--reload"]
