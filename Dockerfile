FROM debian:latest



RUN apt update && apt upgrade -y

RUN apt install git curl python3-pip ffmpeg -y

RUN pip3 install -U pip

RUN cd /

RUN pip install git+https://github.com/openai/whisper.git

RUN git clone https://github.com/mdkawsar-rachel/whisper-openai.git

RUN cd whisper-openai

WORKDIR /whisper-openai

CMD python3 main.py
