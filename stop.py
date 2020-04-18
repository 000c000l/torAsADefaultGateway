import os

"""
    Flushing the nat table
"""
os.system("sudo iptables -t nat -F OUTPUT")
os.system("sudo iptables -t filter -F OUTPUT")

"""
    Stopping tor
"""
os.system("sudo /etc/init.d/tor stop > /dev/null")