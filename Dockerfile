FROM python:3.8

COPY . /app
WORKDIR /app
RUN pip install healthcheck
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python"]
CMD ["server1.py"]