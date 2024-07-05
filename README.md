# Starter for FastAPI
This repo is nothing more than instructions for the first level of a FastAPI app. Fork the repo.

# Installation Instructions
- Use python 3.11
- Using Poetry:
  - add [FastAPI](https://github.com/tiangolo/fastapi)
  - add [gunicorn](https://github.com/benoitc/gunicorn)
  - add [locust](https://github.com/locustio/locust)

# Application
Setup the application based on the FastAPI docs. Prepare one `GET` route for `/status` and have it return `{'message': 'System is healthy'}`

# Locust
Use the [documentation](https://docs.locust.io/en/stable/quickstart.html) to prepare a `locustfile.py` that calls the `/status` endpoint.

# Testing
Locust test your app with:

## Record Keeping
Each individual computer will have different results, but there should be consistency in the ratios between all engineers. Keep track of all settings and results.

## Single Worker
Run `fastapi dev <python file>` in a terminal.

Run `locust --processes 4` in another terminal and open the web interface at http://0.0.0.0:8089.

Set locust to:
- `60 users`
- `10 ramp up`
- Host will be what FastAPI told you (probably `http://127.0.0.1:8000`)
- Under advanced settings type `30s`.

Record results, specifically: # of Requests, Fails, 95 percentile, Average, Max, and Current RPS.

## Multiple Workers
NOTE: If you select "New" from the interface it will put the two runs next to each other (great for later tests).

Run `gunicorn app:app -b 127.0.0.1:8000 --pythonpath app -k uvicorn.workers.UvicornWorker -w 4`

Run `locust --processes 4` in another terminal and open the web interface at http://0.0.0.0:8089.

Set locust to:
- `60 users`
- `10 ramp up`
- Host will be what FastAPI told you (probably `http://127.0.0.1:8000`)
- Under advanced settings type `30s`.

Record results, specifically: # of Requests, Fails, 95 percentile, Average, Max, and Current RPS.

## Experiment
Try any other combinations you think may be interesting.
