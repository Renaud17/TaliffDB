import pip
import os

def install(package,y):
    print(y+1)
    pip.main(['install', package])
    os.system('sudo pip install taliffdb')

install('taliffdb',0)

from distutils.core import setup
'''setup(
  name = 'TaliffDB',
  packages = ['TaliffDB'], # this must be the same as the name above
  version = '0.1',
  description = 'A server for sqlite3',
  author = 'Michael Ilie',
  author_email = 'mcilie@icloud.com',
  url = 'https://github.com/peterldowns/mypackage', # use the URL to the github repo
  download_url = 'https://github.com/peterldowns/mypackage/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
)'''
