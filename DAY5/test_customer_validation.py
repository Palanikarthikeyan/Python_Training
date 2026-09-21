import pytest

@pytest.fixture
def customer():
    return {"id":101,"name":"Raj","balance":10000}

def test_customer_id(customer):
    '''verify customer ID Only'''
    assert customer['id'] == 101

def test_customer_name(customer):
    '''verfiy customer name'''
    assert customer['name'].title() == 'Raj'

def test_customer_balance(customer):
    assert customer['balance'] >5000000
    