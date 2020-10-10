import pathlib
from setuptools import setup, find_packages
import paybyphone_api

HERE = pathlib.Path(__file__).parent

VERSION = paybyphone_api.__version__
PACKAGE_NAME = 'paybyphone_api'
AUTHOR = 'Anatole Callies'
AUTHOR_EMAIL = 'anatole@callies.fr'
URL = 'https://github.com/anatolec/PayMobile'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'This package allows you to automate parking payments in a major cities that use paybyphone. It is based on the selenium web driver.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'selenium'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )