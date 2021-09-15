import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="cicada",
    version=str(open( # oh yes I did
        os.path.join(os.path.dirname(__file__), ".git", "logs", "HEAD")
    ).read().count("\n")),
    description="This library contains a selection of tools for performing high level operations on the LiberPrimus",
    author="Taiiwo"
)
