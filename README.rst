jviewer
=======

|black|
|tests|
|mypy|
|lint|

Simple realtime viewer for journald.

This project was created as example of streaming data from flask application.


Additional requirements
-----------------------

Any GNU/Linux distribution based on `systemd`.
`libsystemd-dev` or it's equivalent must be installed in your system.


Run the application
-------------------

First of all, `poetry <https://python-poetry.org>`_ needs to be installed.
On most GNU/Linux systems just run this command:

.. code::

   python3 -m pip install --user poetry

Then, install project dependencies:

.. code::

   poetry install

Finally, run the application:

.. code::

   poetry run flask run

After application startup, it will be available at `localhost:5000 <http://localhost:5000>`_.

Usage
-----

Just type systemd unit name in field on index page and click `submit`.

.. image:: media/jviewer.gif
   :alt: Preview



Tests
-----

.. code::

   poetry run python -m pytest


Run with gunicorn in production
-------------------------------

**WARNING**: To work normally with this application gunicorn must be used
with async, `gevent` for example, or threaded worker - `gthread`.

Just copy `.secrets.toml.example` to `.secrets.toml` and run:

.. code::

   poetry run gunicorn jviewer.wsgi



.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

.. |tests| image:: https://github.com/TitaniumHocker/jviewer/workflows/tests/badge.svg

.. |mypy| image:: https://github.com/TitaniumHocker/jviewer/workflows/mypy/badge.svg

.. |lint| image:: https://github.com/TitaniumHocker/jviewer/workflows/lint/badge.svg
