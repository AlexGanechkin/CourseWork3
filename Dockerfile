FROM python:3.10-slim

WORKDIR /copy
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY data data
COPY static static
COPY templates templates
COPY logs logs

COPY app.py api_views.py utils.py views.py ./

CMD flask run -h 0.0.0.0 -p 80