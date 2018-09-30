from setuptools import setup, find_packages

setup(name='texformatter',
      version='0.1',
      description='A package for formatting numbers and tables for use in TeX documents.',
      url='https://github.com/cdkharris/texformatter.git',
      author='Camilla D. K. Harris',
      author_email='cdha@umich.edu',
      license='GNU AGPLv3',
      packages=find_packages(),
      python_requires='>=3',
      zip_safe=False)
