Atlas Meta
==========

Project to store metadata for dataset imports. It has API endpoints to update this metadata from other projects, and an enpoint to fetch a html template that contains the stored data.

Requirements
------------

* Docker-Compose (required)


Developing
----------

Use `docker-compose` to start a local database.

	(sudo) docker-compose start

or

	docker-compose up

The API should now be available on http://localhost:8101/

The Database should now be available on 127.0.0.1:5405

