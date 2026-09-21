'''CRM test case'''

def test_customer():
    cus_name = "klabs"
    assert cus_name == "KLABS" or cus_name == "klabs"

def test_customerrecord():
    cus_record = 150
    assert cus_record > 100
    
def test_report():
    assert 500 == 500
    
def test_repolog():
    fname = "/var/log/repo.log"
    assert fname == "/var/log/repo.log"

def test_calculation():
    assert 10+20*3
    
