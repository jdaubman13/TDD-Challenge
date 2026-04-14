def validate_ticket(code):
    if len(code) != 8:
        return False 
    elif type(code) != str:
        raise TypeError("Tickets must be a string")
    elif 


def get_ticket_tier(code):
    pass

def calculate_total(prices, discount=0):
    pass
    
