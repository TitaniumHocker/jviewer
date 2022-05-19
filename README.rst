jviewer
=======

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

.. image:: https://github.com/TitaniumHocker/jviewer/workflows/tests/badge.svg

.. image:: https://github.com/TitaniumHocker/jviewer/workflows/mypy/badge.svg

.. image:: https://github.com/TitaniumHocker/jviewer/workflows/lint/badge.svg

Simple realtime viewer for journald.

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


Usage
-----

Just type systemd unit name in field on index page and click `submit`.

