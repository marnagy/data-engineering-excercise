FROM python:3.11-buster as base

LABEL version="0.1" maintainer="Marek Nagy"

RUN apt update && app install -y --no-install-recommends build-essential gcc libsndfile1

WORKDIR /app
COPY requirements.txt extract_vectors.py process.py ./
RUN pip install -r requirements.txt

FROM base as dev
# expects mounted volume on /app
RUN python3 extract_vectors.py
RUN python3 process.py
EXPOSE 8000
# not checked
CMD ["sh", "run_dev.sh"]

FROM base as prod
COPY ./* .
EXPOSE 8000
# not checked, but use WSGI server instead of the built-in one
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:flask_app"]