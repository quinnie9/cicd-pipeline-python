"""Clientes y envío de formularios con CSRF activado."""

import re

import pytest

from app.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


@pytest.fixture
def csrf_token(client):
    page = client.get("/").get_data(as_text=True)
    return re.search(r'name="csrf_token" value="([^"]+)"', page).group(1)


@pytest.fixture
def post_form(client, csrf_token):
    def submit(data):
        return client.post("/", data={**data, "csrf_token": csrf_token})

    return submit
