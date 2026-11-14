"""La aplicación rechaza formularios sin un token válido para la sesión."""

import re

from app.app import app

FORM = {"num1": "2", "num2": "3", "operacion": "sumar"}


def test_post_without_csrf_is_rejected(client):
    response = client.post("/", data=FORM)
    assert response.status_code == 400
    assert b"CSRF token is missing" in response.data


def test_post_with_tampered_csrf_is_rejected(client, csrf_token):
    response = client.post("/", data={**FORM, "csrf_token": csrf_token + "invalid"})
    assert response.status_code == 400
    assert b"CSRF token is invalid" in response.data


def test_csrf_from_another_session_is_rejected():
    with app.test_client() as first_client:
        page = first_client.get("/").get_data(as_text=True)
        csrf_token = re.search(r'name="csrf_token" value="([^"]+)"', page).group(1)
    with app.test_client() as other_client:
        other_client.get("/")
        response = other_client.post("/", data={**FORM, "csrf_token": csrf_token})
    assert response.status_code == 400
    assert b"CSRF tokens do not match" in response.data
