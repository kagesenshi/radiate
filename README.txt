Deploying
===========

Radiate comes with a buildout configuration which allow you to deploy this
quickly::

  git clone https://kagesenshi@github.com/kagesenshi/radiate.git radiate
  cd radiate
  python bootstrap.py
  ./bin/buildout

The command above will pull the dependencies needed by radiate and install it
in a contained environment.

To start the server, execute::

  ./bin/radiate-admin fg 
