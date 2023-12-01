FROM docker.io/python:slim-bullseye

ADD requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    python -c "import rasterio" && \
    rm -rf /tmp/requirements.txt

ENTRYPOINT []