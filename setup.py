from setuptools import setup

setup(name='async_dns_trawler',
      python_requires='>=3.8.0',
      version='0.1',
      description='DNS Trawler',
      url='http://github.com/gakiwate/async-dns-trawler',
      author='Gautam Akiwate',
      author_email='gakiwate@cs.ucsd.edu',
      license='GPLv2',
      install_requires=[
          'dnspython',
          'PySocks',
          'tldextract',
          'pydgraph',
          'flake8',
          'autopep8',
          'coverage',
          'mypy'
      ],
      zip_safe=False)
