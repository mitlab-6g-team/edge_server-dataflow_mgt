FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /dataflow_mgt
WORKDIR /dataflow_mgt
COPY . /dataflow_mgt

RUN pip install -r ./requirements/base.txt

EXPOSE 30308
CMD python3 manage.py runserver 0.0.0.0:30308
