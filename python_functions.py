

def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100.00, 2) 
   
print('Total tax:', calculate_tax(175, 15))

print('Total tax:', calculate_tax(260.86, 22))