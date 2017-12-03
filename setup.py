VERSION = '0.1.1'

from setuptools import setup, find_packages

setup(name='cryptoz',
      version=VERSION,
      description='cryptoz',
      author='polakowo',
      url='https://github.com/polakowo/cryptoz',
      license='GPL v3',
      packages=find_packages(),
      install_requires=['numpy', 'pandas', 'pytz', 'poloniex', 'matplotlib'],
      python_requires='>=3')