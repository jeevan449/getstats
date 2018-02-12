# from setuptools import setup
 
# setup(
#      name='getstats',    # This is the name of your PyPI-package.
#      version='0.1',                          # Update the version number for new releases
#      scripts=['GetStats.py']                  # The name of your scipt, and also the command you'll be using for calling it
# )


from distutils.core import setup

setup(
    # Application name:
    name="getstats",

    # Version number (initial):
    version="1.0.0",

    # Application author details:
    author="Jeevan Chaitanya",
    author_email="jeevan449@hotmail.com",

    # Packages
    packages=["getstats"],

    # Include additional files into the package
    include_package_data=True,


    # license="LICENSE.txt",
    description="Useful towel-related stuff.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    # install_requires=[
    #     "",
    # ],
)