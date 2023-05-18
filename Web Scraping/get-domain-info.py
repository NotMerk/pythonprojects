import whois

domain='www.noodou.com'
domain_info = whois.whois(domain)

def check_reg(name):
    try:
        domain_info = whois.whois(name)
        return True
    except:
        return False

for key, value in domain_info.items():
    print(key, ':', value)

