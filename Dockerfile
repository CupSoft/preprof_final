FROM python:3.11

WORKDIR /app

RUN pip install -U pip wheel setuptools
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0", "main:app"]