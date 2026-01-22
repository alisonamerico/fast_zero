from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_root_deve_retornar_ok_e_ola_mundo():
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}


def test_root_deve_retornar_html():
    response = client.get('/html')
    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
        <html>
          <head>
            <title> Nosso olá mundo!</title>
          </head>
          <body>
            <h1> Olá Mundo </h1>
          </body>
        </html>"""
    )
