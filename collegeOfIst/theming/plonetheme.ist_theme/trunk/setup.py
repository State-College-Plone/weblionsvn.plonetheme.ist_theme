from setuptools import setup, find_packages
import os

version = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 
    'plonetheme', 'ist_theme', 'version.txt')).read().strip()

setup(name='plonetheme.ist_theme',
    version=version,
    description="Theme Product for the College of Information Sciences and Technology",
    long_description=open("README.txt").read() + "\n" +
                     open("HISTORY.txt").read(),
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
      "Framework :: Plone",
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='',
    author='WebLion Documentation Group, Penn State',
    author_email='support@weblion.psu.edu',
    url='http://weblion.psu.edu/',
    dependency_links = [
       'https://weblion.psu.edu/svn/weblion/weblion/AD54Elements/dist/', 
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plonetheme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      'setuptools',
      'Products.AD54Elements',
      ],
    entry_points="""
      [z3c.autoinclude.plugin]
	  target = plone
      """,
    )