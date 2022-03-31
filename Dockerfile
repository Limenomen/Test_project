FROM python:3.9


RUN apt update; apt install -y supervisor vim npm

ADD requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt; rm /tmp/requirements.txt

COPY . /opt/app
WORKDIR /opt/app

EXPOSE 80
ENV PYTHONUNBUFFERED 1

COPY supervisor/supervisord.conf /etc/supervisor/supervisord.conf
COPY supervisor/app.conf /etc/supervisor/conf.d/app.conf

VOLUME /data/
VOLUME /static/

CMD  rm -rf static; ln -s /static static; \
     /usr/bin/supervisord -c /etc/supervisor/supervisord.conf --nodaemon