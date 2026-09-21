import pytest

def calculate_loan_emi(pricipal,rate,years):
    monthly_rate = rate /(12 * 100)
    months = years * 12
    emi = (pricipal * monthly_rate *(1+monthly_rate) ** months /((1+monthly_rate)**months - 1))
    return round(emi,2)

def test_loan_emi():
    emi = calculate_loan_emi(100000,8.5,20)
    assert emi == 8675.26

