FROM ubuntu
  
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONBUFFERED=1
RUN apt-get update
RUN apt install -y python3-dev python3-pip  python3-opencv vim-tiny  libopencv-dev mosquitto-clients
RUN pip3 install Cython
RUN pip3 install numpy
RUN pip3 install paho-mqtt
# example from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
COPY cam.py cam.py
COPY data data

CMD ["python3","cam.py"]
