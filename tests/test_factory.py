from urllib import response
import pytest

from xfil import create_app

def test_config():
    assert create_app()

def test_hello(client):
    response = client.get("/hello")
    assert response.data == b"Hello World"