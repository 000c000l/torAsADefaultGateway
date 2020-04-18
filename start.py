import os
os.system("sudo /etc/init.d/tor start > /dev/null")
"""
    for Nat
"""
os.system("sudo iptables -t nat -F OUTPUT")
os.system("sudo iptables -t nat -A OUTPUT -m state --state ESTABLISHED -j RETURN")
os.system("sudo iptables -t nat -A OUTPUT -m owner --uid debian-tor -j RETURN")
"""
    For redirecting the tcp and udp packets from port 53 to 9061
"""
os.system("sudo iptables -t nat -A OUTPUT -p udp --dport 53 -j REDIRECT --to-ports 9061")
os.system("sudo iptables -t nat -A OUTPUT -p tcp --dport 53 -j REDIRECT --to-ports 9061")
"""

"""
os.system("sudo iptables -t nat -A OUTPUT -d 10.66.0.0/255.255.0.0 -p tcp -j REDIRECT --to-ports 9051")
os.system("sudo iptables -t nat -A OUTPUT -p tcp -j REDIRECT --to-ports 9051")
"""
    for Filter
"""
os.system("sudo iptables -t filter -F OUTPUT")
os.system("sudo iptables -t filter -A OUTPUT -m state --state ESTABLISHED -j ACCEPT")
os.system("sudo iptables -t filter -A OUTPUT -m owner --uid debian-tor -j ACCEPT")
"""
    Accepting the packets coming from port 9061
"""
os.system("sudo iptables -t filter -A  OUTPUT -p udp --dport 9061 -j ACCEPT")
os.system("sudo iptables -t filter -A  OUTPUT -p tcp --dport 9061 -j ACCEPT")
"""

"""
os.system("sudo iptables -t filter -A OUTPUT -d 10.66.0.0/255.255.0.0 -p tcp -j ACCEPT")
os.system("sudo iptables -t filter -A OUTPUT -p tcp -j ACCEPT")
"""
    Rejecting the udp and icmp packets coming any other port other than 9061
"""
os.system("sudo iptables -t filter -A OUTPUT -p udp -j REJECT")
os.system("sudo iptables -t filter -A OUTPUT -p icmp -j REJECT")

