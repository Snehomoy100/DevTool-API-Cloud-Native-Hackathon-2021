FROM python:3.7

WORKDIR /api
ENV FLASK_APP = app.py
ENV FLASK_RUN_HOST = 0.0.0.0

ADD . /
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "/api/app.py"]
