products = {'candy':10,"juice": 5,"pen":50}

def check(name, qtt):
        if name in products and qtt<=products[name]:
            return True
        else:
            return False
check("pen", 8)

