import os
from pie import *

# Get OS-specific partial path
VENV_TEST = os.path.join(".", "venv", "test")

@task
def build():
    cmd(r"python setup.py bdist_wheel clean --all")


@task
def createVenvs():
    venv(VENV_TEST).create()


@task
def setup():
    createVenvs()
    updatePackages()


@task
def test():
    with venv(VENV_TEST):
        cmd(r"python -m pytest -s --cov-report term --cov-report html --cov=agsconfig .\\tests")


@task
def updatePackages():
    with venv(VENV_TEST):
        pip(r"install -U pip")
        pip(r"install -U -r requirements.test.txt")
        pip(r"install -U -r requirements.txt")


@task([OptionsParameter('version')])
def upload(version):
    cmd(r'python -m twine upload dist\agsconfig-{}-py2.py3-none-any.whl'.format(version))
