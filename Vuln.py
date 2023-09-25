import os
import sys
import socket
import datetime
import subprocess
import ipaddress


def print_jerry_banner():
    banner = """
  ______________               _____      ______  
___  __ \__  /_______ __________(_)________  /__
__  / / /_  __ \  __ `/_  ___/_  /_  ___/_  //_/
_  /_/ /_  / / / /_/ /_  /   _  / / /__ _  ,<   
/_____/ /_/ /_/\__,_/ /_/    /_/  \___/ /_/|_|  
    """
    print(banner)


def print_menu():
    print("\nOptions:")
    print("[0] Ping Scan (Check Whether Host is Up)")
    print("[1] Simple Port Scan")
    print("[2] Stealth Port Scan")
    print("[3] Version Detection")
    print("[4] Whois Lookup")
    print("[5] OS Scan")
    print("[6] Nslookup")
    print("[7] Vulnerability Scan using All Ports")
    print("[8] Check Directories and Subdomains (Dirb) (http)")
    print("[8s] Check Directories and Subdomains (Dirb) (https)")
    print("[9] Nikto Tool")
    print("[10] SQLMAP (Check for SQL Injection Vulnerabilities)")
    print("[11] Aggressive Scan (or) Deep Scan")
    print("[12] Discovering Network")
    print("[f] Fix Missing Files and Install Required Tools")
    print("[x] EXIT")


def run_ping_scan(ip_target):
    response = os.system("fping -c 4 {ip_target}")
    if response == 0:
        print("Host is up.")
    else:
        print("Host is down.")


def run_simple_port_scan(ip_target):
    subprocess.run(["nmap", "-p1-1000", ip_target,"-vv"])


def run_stealth_port_scan(ip_target):
    subprocess.run(["nmap", "-sS", ip_target])


def run_version_detection(ip_target):
    subprocess.run(["nmap", "-sV", "-T4", ip_target])


def run_whois_lookup(ip_target):
    subprocess.run(["whois", ip_target])


def run_os_scan(ip_target):
    subprocess.run(["nmap", "-O", "-T4", ip_target])


def run_nslookup(ip_target):
    subprocess.run(["nslookup", ip_target])


def run_vulnerability_scan(ip_target):
    subprocess.run(["nmap", "--script=vuln", "-sC", "-p-", ip_target])


def run_dirb(ip_target, protocol):
    url = f"{protocol}://{ip_target}"
    subprocess.run(["dirb", url])


def run_nikto(ip_target):
    subprocess.run(["nikto", "-host", ip_target])


def run_sqlmap(ip_target):
    subprocess.run(["sqlmap", ip_target])


def run_aggressive_scan(ip_target):
    subprocess.run(["nmap", "-sV", "-A", "-p-", "-T4", ip_target])


def run_network_discovery(ip_target):
    subprocess.run(["sudo", "netdiscover", "-r", ip_target])


def main():
    print_jerry_banner()
    print("Vulnerability Detection Tool")
    print("CREATED BY: Dharick")
    print("Welcome to the vulnerability scanner:)")
    while True:
        #print("\nToday is", datetime.date.today())
        #host = socket.gethostname()
       # ip_address = socket.gethostbyname(host)
      #  print(f"Hostname: {host} ({ip_address})")
        try:
            ip_target = input("Enter Target IP Address: ")
            ipaddress.IPv4Address(ip_target) 
        except ipaddress.AddressValueError:
            print("Invalid IP Address. Quitting...")
            sys.exit(1)
        print_menu()
        option = input("Enter your Option: ")

        if option == "0":
            run_ping_scan(ip_target)
        elif option == "1":
            run_simple_port_scan(ip_target)
        elif option == "2":
            run_stealth_port_scan(ip_target)
        elif option == "3":
            run_version_detection(ip_target)
        elif option == "4":
            run_whois_lookup(ip_target)
        elif option == "5":
            run_os_scan(ip_target)
        elif option == "6":
            run_nslookup(ip_target)
        elif option == "7":
            run_vulnerability_scan(ip_target)
        elif option == "8":
            run_dirb(ip_target, "http")
        elif option == "8s":
            run_dirb(ip_target, "https")
        elif option == "9":
            run_nikto(ip_target)
        elif option == "10":
            run_sqlmap(ip_target)
        elif option == "11":
            run_aggressive_scan(ip_target)
        elif option == "12":
            run_network_discovery(ip_target)
        elif option == "f":
            subprocess.run(
                ["sudo", "apt-get", "install", "-y", "nmap", "nslookup", "whois", "ipcalc", "nikto", "dirb", "sqlmap"])
            print("Done")
        elif option == "x":
            print("Quitting...")
            sys.exit(0)
        else:
            print("Invalid option. Please select a valid option.")


if __name__ == "__main__":
    main()
