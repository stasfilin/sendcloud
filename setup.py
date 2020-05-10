from os.path import dirname, join

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

from sendcloud import __version__

with open(join(dirname(__file__), "requirements/base.txt")) as f:
    required = f.read().splitlines()

with open(join(dirname(__file__), "requirements/development.txt")) as f:
    required_development = f.read().splitlines()


class PyTest(TestCommand):
    user_options = []

    def run(self):
        import subprocess
        import sys

        errno = subprocess.call([sys.executable, "-m", "pytest", "tests", "-s"])
        raise SystemExit(errno)


setup(
    name="sendcloud-python",
    version=__version__.__version__,
    license="MIT",
    url="https://github.com/stasfilin/sendcloud",
    author="Stanislav Filin",
    py_modules=["sendcloud"],
    packages=find_packages(include=["sendcloud", "sendcloud.*"]),
    install_requires=required,
    extras_require={"develop": required + required_development},
    cmdclass=dict(test=PyTest),
)
