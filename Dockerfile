FROM python:3.6.1-alpine
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install -r requirements.txt
CMD ["python","./manage.py"]