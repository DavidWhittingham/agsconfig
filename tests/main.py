""" Execute all of the tests. Mostly for pytest-cov"""
from types import ModuleType
from os.path import abspath, dirname

import pytest

def importable(module):
    try:
        m = __import__(module, globals(), locals())
        return type(m) is ModuleType
    except ImportError:
        return False

def runtests():
    cmd = ["-r fE"]
    thisDir = dirname(abspath(__file__))

    if importable("pytest_cov"):
        cmd.append("--cov=agsconfig")
        cmd.append("--cov-report=term")
        cmd.append("--cov-report=html")

    cmd.append(thisDir)
    
    pytest.main(cmd)
    
if __name__ == "__main__":
    runtests()