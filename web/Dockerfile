FROM python:3.12-bookworm
LABEL maintainer="datapunt@amsterdam.nl"

ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH=/root/.local/bin:$PATH
ENV PATH=/app/.venv/bin:$PATH

WORKDIR /app

EXPOSE 8000

RUN apt-get update && apt-get install -y \
	build-essential \
	python3-dev \
	netcat-openbsd \
	gdal-bin \
	libpcre3 libpcre3-dev pipx\
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
	&& adduser --system datapunt \
	&& mkdir -p /static \
	&& chown datapunt /static

RUN pipx install poetry==1.8

COPY atlas_meta /app

RUN poetry install
RUN python manage.py collectstatic --noinput

CMD ["uwsgi", "uwsgi.ini"]
