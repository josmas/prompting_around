import pytest
from promptingaround.app import Application

def test_app_main():
    assert Application().run() == 0