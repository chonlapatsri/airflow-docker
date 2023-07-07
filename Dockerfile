FROM apache/airflow:2.6.2-python3.10
COPY requirement.txt /requirement.txt

RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirement.txt