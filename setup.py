import os
from setuptools import setup

read = lambda fname: open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-gobalrequest",
    version = "0.0.5",
    author = "Jonatan Alexis Anauati",
    author_email = "barakawins@gmail.com",
    description = ("A django middleware and a helper to expose globally the "
                   "django request  object."),
    license = "BSD",
    keywords = "web django middleware",
    #url = "http://packages.python.org/an_example_pypi_project",
    packages=['jaa','jaa/django','jaa/django/globalrequest'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

