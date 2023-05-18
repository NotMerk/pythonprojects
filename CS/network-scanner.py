from argparse import ArgumentParser
from scapy.all import srp
from scapy.layers.l2 import ARP, Ether

# # parser = ArgumentParser(
# #     prog="Network Scanner",
# #     description="This is a network scanner that uses arp requests.",
# #     epilog=""
# # )
# #
# # # set up help menu
# # parser.add_argument("-t", "--target", help="Use the syntax -t to specify your target. Must be in CIDR Notation",
# #                     required=True)
# #
# # # parsing command line arguments, needed according to argparse python page
# # args = parser.parse_args()
#
# # change target to whatever IP space you want to scan
# target_ip = args.target

# change target to whatever IP space you want to scan
target_ip = input("Enter IP Address > ")

# create ARP packet
arp = ARP(pdst=target_ip)

# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp

# stack them together
result = srp(packet, timeout=3, verbose=0)[0]

# a list of clients, we will fill this in the upcoming loop
clients = []

for sent, received in result:
    # for each response, append ip and mac address to `clients` list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# print clients
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))