# Inserter
This script reads an array from a JSON file and insert each register in a local elasticsearch.

## Virtualenv
It's highly recommended to use a virtualenv check it [here](https://virtualenv.pypa.io/en/latest/).

## Setup
After activating the virtualenv, run:
```
$ pip install -r requirements.txt
```

## Running it
```
$ python inserter.py
```

> The docker compose file uses partially the code from [here](https://github.com/maxyermayank/docker-compose-elasticsearch-kibana/blob/master/docker-compose.yml)
