FROM python:3.9
WORKDIR /src
COPY app ./app
COPY .env .
EXPOSE 8000
RUN pip3 install -r app/requirements.txt
ENTRYPOINT uvicorn app.main:app --host localhost --port 8000 --reload