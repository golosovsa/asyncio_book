#!make
include secrets.env

POSTGRES_DB ?= products
POSTGRES_USER ?= postgres

run-postgres:
	docker run \
		--detach \
		--rm \
		--name postgres \
		--publish 5432:5432 \
		--env POSTGRES_DB=$(POSTGRES_DB) \
		--env POSTGRES_USER=$(POSTGRES_USER) \
		--env POSTGRES_PASSWORD=$(POSTGRES_PASSWORD) \
		postgres:15.4-alpine3.18
	timeout 30s bash -c "until docker exec postgres pg_isready ; do sleep 5 ; done"

stop-postgres:
	docker stop postgres || true && docker rm postgres || true

download-ngrams:
	wget https://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-1gram-20120701-a.gz
	gunzip googlebooks-eng-all-1gram-20120701-a.gz
	rm -f googlebooks-eng-all-1gram-20120701-a.gz

database: run-postgres
	python src5_3.py
	python src5_4.py
	python src5_5.py
	python src5_6.py
