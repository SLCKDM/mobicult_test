from app.tests.conftest import client

test_currencies = [
    dict(id='TST1'),
    dict(id='TST2'),
    dict(id='TST3'),
]


def test_create_view_correct():
    for payload in test_currencies:
        response = client.post('currency/create', json=payload)
        assert response.status_code == 200
        assert response.json().items() == payload.items()


def test_get_view():
    response = client.get('currency/')
    data = response.json()
    assert response.status_code == 200
    assert type(data) == list
