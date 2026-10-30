allowed_str = '10 20 30'
incoming_str = '20 40 10 50'

allowed = set(allowed_str.split())
incoming = incoming_str.split()

for ip in incoming:
    if ip in allowed:
        print('OK')
    else:
        print('ADDED')
        allowed.add(ip)
