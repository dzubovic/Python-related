"""
first install python-whois with pip install python-whois
more info on https://pypi.org/project/python-whois/
"""
import whois

host = input('Host:') 
res = whois.whois(host)
with open("domaininfo.txt", "w") as out_file:
    out_string = "'"
    out_string += (host)
    out_string += "','" + res.registrar
    out_string += "','" + str(res.name_servers[0])
    out_string += "','" + str(res.name_servers[1])
    out_file.write(out_string)
print ("Domain: ", host)
print ("Registrar: ", res.registrar)
print ("Creation date: ", res.creation_date)
print ("Expiration date: ", res.expiration_date)
print ("Name servers: ", res.name_servers)