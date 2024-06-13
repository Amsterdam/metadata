FROM python:3.12-bookworm
LABEL maintainer="datapunt@amsterdam.nl"

ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH=/root/.local/bin:$PATH

EXPOSE 8000

RUN apt-get update && apt-get install -y \
	netcat-openbsd \
	gdal-bin \
	libpcre3 libpcre3-dev pipx\
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
	&& adduser --system datapunt \
	&& mkdir -p /static \
	&& chown datapunt /static

RUN pipx install poetry==1.3.2
# USER datapunt

WORKDIR /app
COPY atlas_meta /app
RUN poetry install --no-root --no-dev

CMD ["poetry", "run", "gunicorn", "atlas_meta.wsgi:application", "--bind", "0.0.0.0:8000"]
