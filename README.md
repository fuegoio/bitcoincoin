# BitCoinCoin

BitCoinCoin is a fake cryptocurrency trading platform on which the rates of the cryptocurrencies are taken from the real world. You can buy and sell your favorite cryptocurrencies directly on the platform and watch your value evolve with time, compare your score with every one and create or join banks together to merge efforts.

## Getting started

To launch the infrastructure needed (database), we use Docker and Docker-compose :

```
$ docker-compose up -d
```

### Back-end

To setup the backend, we need first to create a virtualenv and install the requirements once :

```
$ cd back/
$ virtualenv --python=python3 venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

The backend has two processes that can be run from the same codebase : the HTTP API and a Celery worker that is gonna process tasks in background.

#### API

The API can be launched with the `web.py` file :

```
$ cd back/
$ source venv/bin/activate
(venv) $ python web.py
```

#### Worker

The Celery worker can be launched with the `tasks.py` file :

```
$ cd back/
$ source venv/bin/activate
(venv) $ python tasks.py
```

This worker is also a Celery beat, which means that it will trigger actions defined by a schedule.
In our case, it is used to refresh the coins database.

### Front-end

To setup the front, we need first to install the requirements once:

```
$ cd front/
$ npm install
```

Then to launch it:

```
$ cd front/
$ npm run serve
```

### Pycharm configuration

In this project, Pycharm is already configured with the right database and the right run configurations: the backend and
the frontend ones.
