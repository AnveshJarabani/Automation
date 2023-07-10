FROM python:3.11

WORKDIR /app

COPY Keywords_finder.py  .
COPY job_data_quality.json  .

RUN pip install nltk 
RUN pip install pandas 


CMD ["python","Keywords_finder.py"]