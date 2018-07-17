FROM continuumio/anaconda3:latest
MAINTAINER Ying Xu "xying@vmware.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
