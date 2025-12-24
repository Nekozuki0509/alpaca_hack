FROM python:3.14.0-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN python -c "import app; app.init_db()"

USER nobody:nogroup

CMD ["gunicorn", "--workers", "8", "--bind", "0.0.0.0:3000", "app:app"]
