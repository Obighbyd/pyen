from distutils.core import setup

setup(
    name='pyen',
    version='1.1', 
    description='simple client for The Echo Nest',
    author="@plamere",
    author_email="paul@echonest.com",
    url='http://github.com/plamere/pyen',
    install_requires=['requests>=1.0',],
    py_modules=['pyen'],)