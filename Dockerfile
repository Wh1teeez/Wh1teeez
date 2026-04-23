FROM python:3.11
WORKDIR /site_radnaev
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "radnaev.wsgi:application", "--bind", "0.0.0.0:8000"]