FROM continuumio/miniconda3

WORKDIR /app
COPY server .

RUN pip3 install -r requirements.txt

CMD ["python3", "api.py"]
