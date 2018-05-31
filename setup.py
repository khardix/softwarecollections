#!/usr/bin/env python3
# encoding: utf-8

from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as readme:
    long_description = readme.read()

METADATA = dict(
    name="softwarecollections",
    version="0.15",
    description="Software Collection Management Website and Utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jakub Dorňák",
    author_email="jdornak@redhat.com",
    url="https://github.com/sclorg/softwarecollections",
)

# Basic package requirements for development instance
REQUIREMENTS = [
    "django-fas",
    "django-markdown2",
    "django-sekizai",
    "django-simple-captcha",
    "django-tagging",
    "django~=1.8.0",
    "flock",
    "py3dns",  # pylibravatar missing dependency workaround
    "pylibravatar",
    "python3-memcached",
    "python3-openid",
    "requests",
]

# Extra requirements for production instance
# Note: Prefer RPM installation to `pip install softwarecollections[production]`
REQUIREMENTS_PRODUCTION = ["mod_wsgi", "psycopg2"]

setup(
    **METADATA,
    python_requires=">=3",
    install_requires=REQUIREMENTS,
    extras_require=dict(production=REQUIREMENTS_PRODUCTION),
    packages=find_packages(),
    include_package_data=True
)
