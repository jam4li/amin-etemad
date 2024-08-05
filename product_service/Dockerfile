FROM python:alpine

ADD ./requirements.txt /product_service/requirements.txt

RUN set -ex \
    && apk add --no-cache --virtual \
        .build-deps \
        build-base \
        mariadb-dev

# Create python's env and Install django's dependencies
RUN set -ex \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /product_service/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
    | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
    | sort -u \
    | xargs -r apk info --installed \
    | sort -u)" \
    && apk add --virtual rundeps $runDeps

# Remove build-deps, because it's no longer needed
RUN set -ex \
    && apk del .build-deps

COPY . /product_service
WORKDIR /product_service

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# run entrypoint.sh
ENTRYPOINT ["/product_service/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]