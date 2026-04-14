import pytest
from ticket_validator import validate_ticket

def test_ticket_is_string():
    result = validate_ticket("TK475246")
    assert result == True 

def test_ticket_is_not_string():
    with pytest.raises(TypeError):
        validate_ticket(12345678)

def test_ticket_is_8_char():
    result = validate_ticket("TK475246")
    assert result == True

def test_ticket_is_not_8_char():
    result = validate_ticket("TK34567")
    assert result == False

def test_ticket_starts_with_tk():
    result = validate_ticket("TK475246")
    assert result == True

def test_ticket_not_starts_with_tk():
    result validate_ticket("5K457875")
    assert result == False

def test_remaining_6_digits():
    result validate_ticket("TK345675")
    assert result == True 

def test_remaining_6_not_digits():
    result = validate_ticket("TK47524A")
    assert result == False




def test_general_tier_true():
    result = get_ticket_tier("TK034686")
    assert result == "General"

def test_general_tier_true2():
    result = get_ticket_tier("TK334686")
    assert result == "General"

def test_vip_tier_true():
    result = get_ticket_tier("TK434686")
    assert result == "VIP"

def test_vip_tier_true2():
    result = get_ticket_tier("TK634686")
    assert result == "VIP"

def test_platinum_tier_true():
    result = get_ticket_tier("TK734686")
    assert result == "Platinum"

def test_platinum_tier_true2():
    result = get_ticket_tier("TK934686")
    assert result == "Platinum"

def test_ticket_is_not_valid():
    with pytest.raises(ValueError):
        get_ticket_tier(12345678)




def test_price_empty():
    with pytest.raises(ValueError):
        calculate_total( , 0.0)

def test_discount_out_of_range():
    with pytest.raises(ValueError):
        calculate_total(10, 1.1)


def test_price_is_not_list():
    with pytest.raises(TypeError):
        calculate_total("10", 0.8)

        
