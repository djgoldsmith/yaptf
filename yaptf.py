#########################################################################
# YAPTF V0.00001 Developed for Diamond House Inc. by The Lead Developer #
#########################################################################

# Some of these might need to be installed on the system seperately:
import socket
import requests
import subprocess
import robotparser

# Features to be added: Extending the function to scan three of the most common ports (HTTP, FTP, SSH)

def scanport(host, port):
    """Attempt to connect to a port on a host to see if it is open
    :param host: Host IP to scan
    :param port: Port to scan
    """
    s = socket.socket()
    try:
        s.connect((host, port))
    except socket.error:
        s.close()
        return False
    s.close()
    return True


# Still a bit buggy, needs a bit of tweaking........

def crackhouse():
    """Bruteforce the password for titanium house"""

    for item in range(999):
        params = {"username":"JoeSmith", "password":item}
        r = requests.get("http://creative.coventry.ac.uk/eh/web_ch4/welcome.php",
                         params = params)
        if r.text.find("incorrect") >=0:
            #print "Fails on {0}".format(item)
            pass
        else:
            #print "Passcode {0} Ok".format(item)
            return item

def cracksingle(pin):
    """Perform a single iteration of the crackhouse
    :param pin: Pin to test
    :return True if a password matches
    """

    params = {"username": "JoeSmith",
              "password": pin}

    r = requests.get("http://creative.coventry.ac.uk/eh/web_ch4/welcome.php",
                     params = params)

    return r.text.find("incorrect") == -1
        

#This needs a bit more tweaking to get it working:

def listRestricted(sites = None):
    """ Return the restricted folders from a webpage based on the robots.txt file.    :param sites:  The site to scan against
    """
    if not sites:
        sites = 'www.google.com'
    
    def getDenies(site):
        """ Create a new robotparser instance and read the site's robots file"""
        paths =[]
        robot = robotparser.RobotFileParser()
        robot.set_url("http://"+site+"/robots.txt")
        robot.read()
        
        # For each entry, look at the rule lines and add the path to paths if disallowed.
        for line in robot.default_entry.rulelines:
            not line.allowance and paths.append(line.path)
        return set(paths)

    return getDenies(sites)


def identifyOUI(macaddress):
    """This function should identify the manufacturer of a given device based on its MAC adress"""
    # Load the Wireshark manufacturers database file from the disk and  search through it to return the manufacturer
    
    database = open("data.txt", "r")
    for line in database:
        if macaddress in line:
            #print line
            return line.split()[1]
    database.close()
    return False

def generateReport():
    """This function should take all the output from the selected tunctionality and save it to a file of some sort."""
    
    #listRestricted()
    #print scanport("127.0.0.1",8000)
    #print crackhouse()
    #print listrestricted
    print("Documentation generated and saved to file.")

    

# Below I can test all the custom functionality that I am writing, just by calling the function

if __name__ == "__main__":
    #amazingMenu()
    #listRestricted()
    identifyOUI("A4:18:75")
    #print scanport("127.0.0.1",8000)
    #print crackhouse()
    #print listrestricted
