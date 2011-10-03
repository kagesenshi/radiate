from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='radiate',
      version=version,
      description="Simple SocketIO push server",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python websocket socketio',
      author='Izhar Firdaus',
      author_email='kagesenshi.87@gmail.com',
      url='http://github.com/kagesenshi/radiate',
      license='http://www.apache.org/licenses/LICENSE-2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'tornado',
          'TornadIO',
          'argh',
          'argparse'
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'console_scripts': [
              'radiate-admin = radiate.admin:main',
           ]
      },
)
