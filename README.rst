
=====================================================
Google App Engine Buildout Demo (gaebuildoutdemo.app)
=====================================================


Requirenments
-------------

- Python with virtualenv
- Pillow dependencies http://pillow.readthedocs.org/en/3.0.x/installation.html#external-libraries


Build Environment
-----------------

::

  cd src
  python bootstrap-buildout.py
  bin/buildout


Commands
--------

Make sure your current directory is inside the ``src`` dir.

``bin/serve`` - Run the google SDK serve with the application

``bin/test`` - Test runner

``bin/deploy-prod`` - Deploy application.




