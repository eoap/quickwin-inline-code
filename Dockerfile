FROM docker.io/python:3.10-slim

ADD requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    python -c "import rasterio" && \
    rm -rf /tmp/requirements.txt

ENTRYPOINT []