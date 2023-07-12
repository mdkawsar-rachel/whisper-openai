FROM debian:latest

RUN apt update && apt upgrade -y

RUN apt install git curl python3-pip ffmpeg -y

RUN pip3 install -U pip

ADD ./ ./

RUN pip install -r requirements.txt

WORKDIR ./

RUN pip install git+https://github.com/openai/whisper.git

CMD python3 api.py
