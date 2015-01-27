""""
Controller class for the various YAPT functions
"""

import yaptf
import socket

def scanports(host, dohttp, dossh, dotelnet):
    """Given a range of ports, scan a host to see if sockets are open"""
    
    #Lookup host if its not an ip
    try:
        int(host[0])
        header = "Port Scan for {0}".format(host)
    except ValueError:
        #In this case its a string thus needs lookig up
        hname = host
        host = socket.gethostbyname(host)
        header = "Port Scan for {0} ({1})".format(hname, host)
    
    ports = []
    if dohttp:
        ports.append(socket.getservbyname("http"))
    if dossh:
        ports.append(socket.getservbyname("ssh"))
    if dotelnet:
        ports.append(socket.getservbyname("telnet"))

    #Then run the checks
    matches = []

    #Quick and dirty lookup to turn T/F into open 
    lookup = {True: "Open",
              False: "Closed"}
    for port in ports:
        
        matches.append([port,
                        socket.getservbyport(port),
                        lookup[yaptf.scanport(host, port)],
              ])
    return header, matches

def lookupmac(mac):
    """Link to the identify OUI part of the toolkit"""
    return yaptf.identifyOUI(mac)

def cracksingle(pin):
    #1-1 link on pin cracking
    return yaptf.cracksingle(pin)

def listrestricted(site = None):
    #List restricted, again another 1-1 mapping
    return yaptf.listRestricted(site)

if __name__ == "__main__":
    scanports("88",None)
    scanports("creative.coventry.ac.uk", None)
        
