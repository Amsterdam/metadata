FROM python:3.7-bookworm
MAINTAINER datapunt@amsterdam.nl

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN apt-get update && apt-get install -y \
	netcat-openbsd \
	gdal-bin \
	libpcre3 libpcre3-dev \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
	&& adduser --system datapunt \
	&& mkdir -p /static \
	&& chown datapunt /static \
	&& pip install uwsgi

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

USER datapunt
COPY atlas_meta /app/

RUN ./manage.py collectstatic
CMD /app/docker-entrypoint.sh
