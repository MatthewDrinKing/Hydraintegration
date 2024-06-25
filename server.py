import requests

# Hydra II device IP address
hydra_ip = "192.168.1.126"

# Ticket commands to send
ticket_commands = """
3/S/Articolo 1//1/1.23/1/
3/S/Articolo 2//1/1.23/2/
3/S/Articolo 3//1/1.23/3/
3/S/Articolo 4//1/1.23/4/
7/1/1//
7/1/1/Note o commenti qui//
7/1/1//
5/1/1///
6/4/8////
0/
"""

# Send ticket commands
response = requests.post(f"http://{hydra_ip}/_fileio?cmd=3", data=ticket_commands, headers={"Content-Type": "text/plain"})
print("Send Ticket Commands Response:", response.status_code, response.text)

# Execute ticket command (response JS disabled)
response = requests.get(f"http://{hydra_ip}/_io?cmd=5&js=0")
print("Execute Ticket Command (JS Disabled) Response:", response.status_code, response.text)

# Execute ticket command (response JS enabled)
response = requests.get(f"http://{hydra_ip}/_io?cmd=5&js=1")
print("Execute Ticket Command (JS Enabled) Response:", response.status_code, response.text)