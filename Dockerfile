FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3-pip openjdk-11-jdk

RUN apt-get install -y wget unzip

RUN pip3 install stanfordcorenlp==3.9.1.1

RUN wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-02-27.zip && unzip stanford-corenlp-full-2018-02-27.zip

RUN pip3 install ai-integration

COPY model.py .
COPY entrypoint.py .

CMD []
ENTRYPOINT ["python3", "entrypoint.py"]

# docker build -t deepaiorg/sentiment-analysis .
