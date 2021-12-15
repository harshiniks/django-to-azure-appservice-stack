from setuptools import find_packages, setup
import os

# Get more https://pypi.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    # Indicate to who your project is directed
    "Environment :: Web Environment",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    # Indicate supported versions, Python 2, Python 3 or both.
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    "Topic :: Internet :: WWW/HTTP :: WSGI",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

EXCLUDE_FROM_PACKAGES = ["project","project.*"]

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

setup(
    name="django-to-azure-appservice-stack",
    version="0.1",
    description="A Django 'Hello World' program deployed in Azure",
    long_description=read('README.rst'),
    classifiers=CLASSIFIERS,
    keywords="stack azure helloworld django",
    author="Harshini K S",
    author_email="harshiniks@github.com",
    maintainer="Harshini K S. Ayaz Qureshi.",
    maintainer_email="ayaz43@github.com",
    url="https://github.com/harshiniks/django-to-azure-appservice-stack",
    license="",
    platforms="OS Independent",
    install_requires=["Django==2.2.3"],
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    zip_safe=False,
    project_urls={
        'Documentation': 'https://docs.djangoproject.com/'
    },
)
