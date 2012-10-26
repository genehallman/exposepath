import os

from setuptools import setup, find_packages

version = '0.1'


def read_file(name):
    return open(os.path.join(os.path.dirname(__file__),
                             name)).read()

readme = read_file('README.rst')
changes = read_file('CHANGES.rst')

setup(name='collective.recipe.exposepath',
      version=version,
      description="Buildout recipe for exposing the working set as an option",
      long_description='\n\n'.join([readme, changes]),
      classifiers=[
        'Framework :: Buildout',
        'Topic :: Software Development :: Build Tools',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        ],
      package_dir={'': 'src'},
      packages=find_packages('src'),
      keywords='',
      author='Gene Hallman',
      author_email='gene@livefyre.com',
      url='https://github.com/genehallman/exposepath',
      license='BSD',
      zip_safe=False,
      install_requires=[
        'zc.buildout',
        'zc.recipe.egg',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [zc.buildout]
      default = collective.recipe.exposepath:Recipe
      """,
      )
