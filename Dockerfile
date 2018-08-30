FROM centos/python-36-centos7
USER root

ADD . .
RUN yum --assumeyes install publican \
    && yum clean all && rm -rf /var/cache/yum \
    && git clone https://github.com/pmkovar/packaging-guide \
    && ./guide-build packaging-guide \
    && ./guide-import packaging-guide

ENV SOFTWARECOLLECTIONS_BASE_DIR=/var/scls \
    DJANGO_SETTINGS_MODULE=softwarecollections.settings

RUN python3.6 -m pip install pipenv \
    && pipenv install --system --deploy \
    && mkdir -p "$SOFTWARECOLLECTIONS_BASE_DIR"/htdocs/{static,media,repos} \
    && django-admin migrate --noinput \
    && django-admin collectstatic --noinput --verbosity=1 \
    && django-admin makeerrorpages
