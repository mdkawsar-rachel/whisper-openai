FROM ubuntu:20.04

RUN apt-get update && apt-get install python python3-pip -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends ffmpeg

ADD ./ ./

RUN pip install -r requirements.txt

WORKDIR ./

CMD ["uvicorn","api:app"]

EXPOSE 8000