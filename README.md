# Reverseshell_Hijack


Execute:
sudo stdbuf --output=0 tcpdump -i any -nnnv "tcp[tcpflags]=(tcp-syn)" | python3 monitor_traffic.py

screen -ls
screen -r <name>

Detach screen-sessions
str+a d



VICTIM -> ROUTER (DNAT) -> SNIFFER


IPTABLES
https://gridscale.io/community/tutorials/tutorial-debian-routergateway-10minuten/
iptables-save > /etc/iptables/rules.v4
iptables-restore > /etc/iptables/rules.v4


# Generated by iptables-save v1.8.7 on Wed Apr 26 13:10:57 2023
*filter
:INPUT ACCEPT [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
-A INPUT -i lo -j ACCEPT
-A INPUT -i enp0s3 -p tcp -m tcp --dport 22 -j ACCEPT
-A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
-A INPUT -i enp0s3 -j DROP
COMMIT
# Completed on Wed Apr 26 13:10:57 2023
# Generated by iptables-save v1.8.7 on Wed Apr 26 13:10:57 2023
*nat
:PREROUTING ACCEPT [0:0]
:INPUT ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
:POSTROUTING ACCEPT [0:0]
-A PREROUTING -i enp0s8 -j DNAT --to-destination 192.168.1.112
-A POSTROUTING -o enp0s3 -j MASQUERADE
COMMIT
# Completed on Wed Apr 26 13:10:57 2023
