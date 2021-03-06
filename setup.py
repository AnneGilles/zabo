import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'Babel',
    'colander',
    'cryptacular',
    'deform',
    'lingua',
    'pyramid',
    'pyramid_beaker',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_mailer',
    'pyramid_tm',
    'python-gnupg',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
]
test_requires = [
    'coverage',
    'nose',
    #'nose-cov',
    'webtest',
]
setup(name='zabo',
      version='0.0',
      description='zabo',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='zabo',
      install_requires=requires+test_requires,
      entry_points="""\
      [paste.app_factory]
      main = zabo:main
      [console_scripts]
      initialize_zabo_db = zabo.scripts.initializedb:main
      """,
      message_extractors={
          'zabo': [
              ('**.py', 'lingua_python', None),
              ('**.pt', 'lingua_xml', None),
          ]
      }
      )
