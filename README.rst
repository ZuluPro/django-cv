=========
Django-CV
=========

.. image :: https://travis-ci.org/ZuluPro/django-cv.svg?branch=master
   :target: https://travis-ci.org/ZuluPro/django-cv
       
.. image:: https://coveralls.io/repos/ZuluPro/django-cv/badge.svg?branch=master
   :target: https://coveralls.io/r/ZuluPro/django-cv?branch=master

.. image:: https://landscape.io/github/ZuluPro/django-cv/master/landscape.svg?style=flat
   :target: https://landscape.io/github/ZuluPro/django-cv/master
      :alt: Code Health

Django application for manage and export your resume.

Install
=======

::

    python setup.py install
    git+git://github.com/ojii/pymaging.git#egg=pymaging
    git+git://github.com/ojii/pymaging-png.git#egg=pymaging-png

Edit your ``settings.py`` for add ``curriculum`` to ``INSTALLED_APPS``: ::

    INSTALLED_APPS = (
        ...
        'curriculum',
        ...
    )


Usage
=====

All data can be filled in Django's administration site or by custom way.

You can export you resume as PDF with administration's action. Select in
details which information you want export and clic. 

You can use or copy the following views for export:

- ``curriculum.views.export_single_page``: For create a single page resume
- ``curriculum.views.export_classic``: For create a classic resume

Or use HTML5 presentation view: ``curriculum.revealjs.views.get_resume``.

Tests
=====

You can run tests with Tox: ::

    tox -e py2.7-rl32-django1.8

Try it quickly
==============

You can test it with its `demo`_ or install yourself as describe above and
launch the following commands: ::

    pip install django
    python tests/runtests.py migrate
    python tests/runtests.py createsuperuser
    # Create your login and password
    python tests/runtests.py runserver 0.0.0.0:8080

Now you can go to http://0.0.0.0:8080 and try the app.

.. _`demo`: https://github.com/ZuluPro/django-cv-demo
