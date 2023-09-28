# Dilarang mengubah file tanpa izin
# FareltZky
import urllib.parse
import tarfile
import urllib.request
import zipfile
import json
import subprocess
import os
import sys
import time
import socket
import shutil
flag = True
argumen = " "
if len(sys.argv) >= 2:
    argumen = sys.argv[1]
    print(f"Argumen yang diberikan: {argumen}")
if argumen == "--start":
    os.system("clear")
    if not os.path.exists("bedrock"):
        print("install server first! Use: python3 main.py --install")
    elif not os.path.exists(os.path.join("bedrock", "bedrock_server")):
        print("file bedrock_server not found!")
    elif not os.path.exists(os.path.join("bedrock", "server.properties")):
        print("file server.properties not found!")
    else:
        envss = {"LD_LIBRARY_PATH": "."}
        subprocess.run(["chmod +x ./bedrock/bedrock_server"], shell=True)
        subprocess.run(["cd bedrock && ./bedrock_server"],
                       env=envss, shell=True)
        ipxbedrock = socket.gethostbyname(socket.gethostname())
        print(f"ip for server:p {ipxbedrock}")
else:
    while flag:

        print("====================°    °======================")
        print("| please select your choice")
        print("|")
        print("| 1. minecraft bedrock server")
        print("| 2. minecraft java server (error,not available)")
        print("| 3. exit")
        print("|")
        print("| by: FareltZky")
        print("| github: github.com/FareltZky")
        print(f"| ip: {socket.gethostbyname(socket.gethostname())}")
        print("====================°    °======================")
        mcsvrmenu = input(" ")

        if mcsvrmenu.isdigit():
            pilihan = int(mcsvrmenu)

            if pilihan == 1:
                os.system("clear")
                while flag:
                    print("====================°    °======================")
                    print(
                        f"| select server version     ip: {socket.gethostbyname(socket.gethostname())}")
                    print("|")
                    print("| 1. Version 1.20")
                    print("| 2. Version 1.19")
                    print("| 3. Version 1.18")
                    print("| 4. Version 1.17")
                    print("| 5. Version 1.16")
                    print("| 9. Run Server       [10]Config      [11] tools")
                    print("|")
                    print("| next Version soon.")
                    print("|                                  by:FareltZky")
                    print("| 0. back          github: github.com/FareltZky")
                    print("====================°    °======================")
                    svrvrch = input(" ")
                    if svrvrch.isdigit():
                        subver = int(svrvrch)
                        if subver == 1:
                            while flag:
                                os.system("clear")
                                print(
                                    "====================°    °======================")
                                print(
                                    f"| select server version      ip: {socket.gethostbyname(socket.gethostname())}")
                                print("|")
                                print("| 1. 1.20.15")
                                print("| 2. 1.20.1")
                                print(
                                    "|                                  by:FareltZky")
                                print(
                                    "| 0. back          github: github.com/FareltZky")
                                print(
                                    "====================°    °======================")
                                input20 = input(" ")
                                if input20.isdigit():
                                    sub20 = int(input20)
                                    if sub20 == 1:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                "Are You Sure Want to Install")
                                            print("1.20.15 Version?")
                                            yn15 = input(" [yes]/[no] :")
                                            if yn15 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-20-15"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-20-15"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                    folname = filenamed.replace(
                                                        ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                        print(
                                                            "extracting success")
                                                        time.sleep(5)
                                                        svrip = socket.gethostbyname(
                                                            socket.gethostname())
                                                        print("Running...")
                                                        print(
                                                            f"Running in ip: {svrip}")
                                                        time.sleep(5)
                                                        os.system("clear")
                                                        envs = {
                                                            "LD_LIBRARY_PATH": "."}
                                                        subprocess.run(
                                                            ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                        subprocess.run(
                                                            ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn15 == "no":
                                                os.system("clear")
                                                break
                                                print("Canceled")
                                            else:
                                                os.system("clear")
                                                print("Unexpected input")
                                    elif sub20 == 2:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                "Are You Sure to Install/Change version")
                                            print("1.20.1??")
                                            yn1201 = input("[yes/no]")
                                            if yn1201 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-20-1"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-20-1"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                        time.sleep(5)
                                                        print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                        print(
                                                            "extracting success")
                                                        time.sleep(5)
                                                        svrip = socket.gethostbyname(
                                                            socket.gethostname())
                                                        print("Running...")
                                                        print(
                                                            f"Running in ip: {svrip}")
                                                        time.sleep(5)
                                                        os.system("clear")
                                                        envs = {
                                                            "LD_LIBRARY_PATH": "."}
                                                        subprocess.run(
                                                            ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                        subprocess.run(
                                                            ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1201 == "no":
                                                os.system("clear")
                                                break
                                                print("Canceled")
                                            else:
                                                os.system("clear")
                                                print("Incorrect Answer")
                                    elif sub20 == 0:
                                        os.system("clear")
                                        print("back")
                                        break
                                    else:
                                        os.system("clear")
                                        print("invalid input")
                                else:
                                    os.system("clear")
                                    print("input must be number")
                        elif subver == 2:
                            os.system("clear")
                            while flag:
                                print(
                                    "====================°    °======================")
                                print("| 1. 1.19.61")
                                print("| 2. 1.19.51")
                                print("| 3. 1.19.31")
                                print("| 4. 1.19.21")
                                print("| 5. 1.19.11")
                                print("| 6. 1.19.1")
                                print(
                                    "|                                 by: FareltZky")
                                print(
                                    "|                  github: github.com/FareltZky")
                                print("| 0. back")
                                print(
                                    "====================°    °======================")
                                sub19 = input(" ")
                                if sub19.isdigit():
                                    subv19 = int(sub19)
                                    if subv19 == 1:
                                        while flag:
                                            os.system("clear")
                                            print(
                                                "Are you sure to install/change version")
                                            print("1.19.61??")
                                            yn1961 = input("[yes/no]: ")
                                            if yn1961 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-19-61"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-19-61"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                        print(
                                                            "extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)

                                            elif yn1961 == "no":
                                                os.system("clear")
                                                break
                                                print("back")
                                            else:
                                                os.system("clear")
                                                print("invalid answer")
                                    elif subv19 == 2:
                                        os.system("clear")
                                        print("1.19.51")
                                        while flag:
                                            print(
                                                "Are you sure to install/change version")
                                            print("1.19.51??")
                                            yn1951 = input("[yes/no]")
                                            if yn1951 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-19-51"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-19-51"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                        print(
                                                            "extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1951 == "no":
                                                os.system("clear")
                                                break
                                                print("canceled")
                                            else:
                                                os.system("clear")
                                                print("invalid answer")
                                    elif subv19 == 3:
                                        os.system("clear")
                                        print(
                                            "Are you sure to install)change version")
                                        print("1.19.31 ??")
                                        yn1931 = input("[yes/no]: ")
                                        if yn1931 == "yes":
                                            flag = False
                                            os.system("clear")
                                            print("wait....")
                                            time.sleep(5)
                                            with open('data-data.json', 'r') as file:
                                                data = json.load(file)
                                                urll = data["minecraft-bedrock-server"]["1-19-31"]["url"]
                                                filenamed = data["minecraft-bedrock-server"]["1-19-31"]["namefile"]
                                                linxurl = urll.replace(
                                                    "bin-win", "bin-linux")

                                                try:
                                                    print(
                                                        "downloading assest....")
                                                    urllib.request.urlretrieve(
                                                        linxurl, filenamed)
                                                    print("download success")
                                                except Exception as e:
                                                    print(f"err: {str(e)}")
                                                    folname = filenamed.replace(
                                                        ".zip", " ")
                                                time.sleep(5)
                                                print("extracting....")
                                                if os.path.exists("bedrock"):
                                                    print(
                                                        "deleting previous file")
                                                    shutil.rmtree("bedrock")
                                                if not os.path.exists("bedrock"):
                                                    os.makedirs("bedrock")
                                                with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                    zip_ref.extractall(
                                                        "bedrock")
                                                    os.remove(filenamed)
                                                    print("extracting success")
                                                time.sleep(5)
                                                svrip = socket.gethostbyname(
                                                    socket.gethostname())
                                                print("Running...")
                                                print(
                                                    f"Running in ip: {svrip}")
                                                time.sleep(5)
                                                os.system("clear")
                                                envs = {"LD_LIBRARY_PATH": "."}
                                                subprocess.run(
                                                    ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                subprocess.run(
                                                    ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                        elif yn1931 == "no":
                                            os.system("clear")
                                            break
                                            print("canceled")
                                        else:
                                            os.system("clear")
                                            print("invalid answer")
                                    elif subv19 == 4:
                                        while flag:
                                            os.system("clear")
                                            print(
                                                "Are you sure install/change version to")
                                            print("1.19.21 version ???")
                                            yn1921 = input("[yes]/[no] ??")
                                            if yn1921 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-19-21"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-19-21"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                        print(
                                                            "extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1921 == "no":
                                                os.system("clear")
                                                break
                                                print("canceled")
                                            else:
                                                os.system("clear")
                                                print("Invalid Answer")
                                    elif subv19 == 5:
                                        while flag:
                                            os.system("clear")
                                            print(
                                                "Are you sure install/change version to")
                                            print("1.19.11 Version ??")
                                            yn1911 = input("[yes] / [no]")
                                            if yn1911 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                print("Configuring File....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-19-11"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-19-11"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                        print(
                                                            "extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1911 == "no":
                                                os.system("clear")
                                                break
                                                print("canceled")
                                            else:
                                                os.system("clear")
                                                print("Invalid Answer")
                                    elif subv19 == 6:
                                        while flag:
                                            os.system("clear")
                                            print(
                                                "Are you sure install/change version to")
                                            print("1.19.1 Version ??")
                                            yn191 = input("[yes] / [no]")
                                            if yn191 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                print("configuring file.....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-19-1"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-19-1"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                        print(
                                                            "extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn191 == "no":
                                                os.system("clear")
                                                break
                                                print("canceled")
                                            else:
                                                os.system("clear")
                                                print("incorrect answer")
                                    elif subv19 == 0:
                                        os.system("clear")
                                        break
                                        print("back")
                                    else:
                                        print("invalid input")
                                else:
                                    print("input must be numbber")
                        elif subver == 3:
                            os.system("clear")
                            while flag:
                                print(
                                    "====================°    °======================")
                                print(
                                    f"| Select a Versions     ip: {socket.gethostbyname(socket.gethostname())}")
                                print("| ")
                                print("|")
                                print("| 1. 1.18.33")
                                print("| 2. 1.18.32")
                                print("| 3. 1.18.11")
                                print("| 4. 1.18.1")
                                print("|")
                                print("|")
                                print("| by: FareltZky")
                                print(
                                    "| github: github.com/FareltZky      [0] back")
                                print(
                                    "====================°    °======================")
                                subver18 = input(" ")
                                if subver18.isdigit():
                                    subv18 = int(subver18)

                                    if subv18 == 1:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                " Are You Sure Install/Change Version To")
                                            print("1.18.33 Version???")
                                            yn1833 = input("[yes] or [no]: ")
                                            if yn1833 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-18-33"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-18-33"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                    print("extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1833 == "no":
                                                os.system("clear")
                                                break
                                                print("Cancelled")
                                            else:
                                                print("invalid input")
                                        # time.sleep(1)
                                    elif subv18 == 2:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                " Are You Sure Install/Change Version To")
                                            print("1.18.32 Version???")
                                            yn1833 = input("[yes] or [no]: ")
                                            if yn1833 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-18-32"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-18-32"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                    print("extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1833 == "no":
                                                os.system("clear")
                                                break
                                            else:
                                                os.system("clear")
                                                print("invalid input")
                                    elif subv18 == 3:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                " Are You Sure Install/Change Version To")
                                            print("1.18.11 Version???")
                                            yn1833 = input("[yes] or [no]: ")
                                            if yn1833 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-18-11"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-18-11"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                    print("extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1833 == "no":
                                                os.system("clear")
                                                break
                                            else:
                                                os.system("clear")
                                                print("invalid input")
                                    elif subv18 == 4:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                " Are You Sure Install/Change Version To")
                                            print("1.18.1 Version???")
                                            yn1833 = input("[yes] or [no]: ")
                                            if yn1833 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-18-1"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-18-1"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                    print("extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1833 == "no":
                                                os.system("clear")
                                                break
                                            else:
                                                os.system("clear")
                                                print("invalid input")
                                    elif subv18 == 0:
                                        os.system("clear")
                                        break
                                        print("back to previous menu")
                                        time.sleep(1)
                                    else:
                                        os.system("clear")
                                        print("incorrect input")
                                else:
                                    os.system("clear")
                                    print("input must be number")
                        elif subver == 4:
                            os.system("clear")
                            while flag:
                                print(
                                    "====================°    °======================")
                                print(
                                    f"| select version         ip: {socket.gethostbyname(socket.gethostname())}")
                                print("|")
                                print(
                                    "| [1] 1.17.41                           [0] Back")
                                print("| [2] 1.17.33")
                                print("| [3] 1.17.31")
                                print("| [4] 1.17.11")
                                print(
                                    "| [5] 1.17.2                       by: FareltZky")
                                print(
                                    "| [6] 1.17.1       github: github.com/FareltZky")
                                print(
                                    "====================°    °======================")
                                subver17 = input(" ")
                                if subver17.isdigit():
                                    subv17 = int(subver17)
                                    if subv17 == 1:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                " Are You Sure Install/Change Version To")
                                            print("1.17.41 Version???")
                                            yn1833 = input("[yes] or [no]: ")
                                            if yn1833 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-17-41"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-17-41"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                    print("extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1833 == "no":
                                                os.system("clear")
                                                break
                                            else:
                                                os.system("clear")
                                                print("invalid input")
                                    elif subv17 == 2:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                " Are You Sure Install/Change Version To")
                                            print("1.17.33 Version???")
                                            yn1833 = input("[yes] or [no]: ")
                                            if yn1833 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-17-33"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-17-33"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                    print("extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1833 == "no":
                                                os.system("clear")
                                                break
                                            else:
                                                os.system("clear")
                                                print("invalid input")
                                    elif subv17 == 3:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                " Are You Sure Install/Change Version To")
                                            print("1.17.31 Version???")
                                            yn1833 = input("[yes] or [no]: ")
                                            if yn1833 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-17-31"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-17-31"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                    print("extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1833 == "no":
                                                os.system("clear")
                                                break
                                            else:
                                                os.system("clear")
                                                print("invalid input")
                                    elif subv17 == 4:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                " Are You Sure Install/Change Version To")
                                            print("1.17.11 Version???")
                                            yn1833 = input("[yes] or [no]: ")
                                            if yn1833 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-17-11"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-17-11"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                    print("extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1833 == "no":
                                                os.system("clear")
                                                break
                                            else:
                                                os.system("clear")
                                                print("invalid input")
                                    elif subv17 == 5:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                " Are You Sure Install/Change Version To")
                                            print("1.17.2 Version???")
                                            yn1833 = input("[yes] or [no]: ")
                                            if yn1833 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-17-2"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-17-2"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                    print("extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1833 == "no":
                                                os.system("clear")
                                                break
                                            else:
                                                os.system("clear")
                                                print("invalid input")
                                    elif subv17 == 6:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                " Are You Sure Install/Change Version To")
                                            print("1.17.1 Version???")
                                            yn1833 = input("[yes] or [no]: ")
                                            if yn1833 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-17-1"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-17-1"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                    print("extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1833 == "no":
                                                os.system("clear")
                                                break
                                            else:
                                                os.system("clear")
                                                print("invalid input")
                                    elif subv17 == 0:
                                        os.system("clear")
                                        break
                                        print("back to previous menu")
                                    else:
                                        print("invalid input")
                                else:
                                    os.system("clear")
                                    print("input must be number")
                        elif subver == 5:
                            os.system("clear")
                            while flag:
                                print(
                                    "====================°    °======================")
                                print(
                                    f"| Select Version         ip: {socket.gethostbyname(socket.gethostname())}")
                                print("|")
                                print("| [1] 1.16.201")
                                print("| [2] 1.16.200")
                                print("| [3] 1.16.101")
                                print(
                                    "| [4] 1.16.100                          [0] Back")
                                print("| [5] 1.16.40")
                                print(
                                    "| [6] 1.16.1                       by: FareltZky")
                                print(
                                    "| [7] 1.16.0       github: github.com/FareltZky")
                                print(
                                    "====================°    °======================")
                                subver16 = input(" ")
                                if subver16.isdigit():
                                    subv16 = int(subver16)
                                    if subv16 == 1:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                " Are You Sure Install/Change Version To")
                                            print("1.16.201 Version???")
                                            yn1833 = input("[yes] or [no]: ")
                                            if yn1833 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-16-201"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-16-201"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                    print("extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1833 == "no":
                                                os.system("clear")
                                                break
                                    elif subv16 == 2:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                " Are You Sure Install/Change Version To")
                                            print("1.16.200 Version???")
                                            yn1833 = input("[yes] or [no]: ")
                                            if yn1833 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-16-200"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-16-200"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                    print("extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)

                                            elif yn1833 == "no":

                                                os.system("clear")
                                                break
                                            else:
                                                print("invalid input")
                                    elif subv16 == 3:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                " Are You Sure Install/Change Version To")
                                            print("1.16.101 Version???")
                                            yn1833 = input("[yes] or [no]: ")
                                            if yn1833 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-16-101"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-16-101"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                    print("extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1833 == "no":
                                                os.system("clear")
                                                break
                                                print("back to preview menu")
                                            else:
                                                os.system("clear")
                                    elif subv16 == 4:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                " Are You Sure Install/Change Version To")
                                            print("1.16.100 Version???")
                                            yn1833 = input("[yes] or [no]: ")
                                            if yn1833 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-16-100"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-16-100"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                    print("extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1833 == "no":
                                                os.system("clear")
                                                break
                                            else:
                                                print(" invalid input")
                                    elif subv16 == 5:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                " Are You Sure Install/Change Version To")
                                            print("1.16.40 Version???")
                                            yn1833 = input("[yes] or [no]: ")
                                            if yn1833 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-16-40"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-16-40"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                    print("extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1833 == "no":
                                                os.system("clear")
                                                break
                                        else:
                                            print("invalid input")
                                    elif subv16 == 6:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                " Are You Sure Install/Change Version To")
                                            print("1.16.1 Version???")
                                            yn1833 = input("[yes] or [no]: ")
                                            if yn1833 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-16-1"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-16-1"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                    print("extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1833 == "no":
                                                os.system("clear")
                                                break
                                            else:
                                                os.system("clear")
                                                print("invalid input")
                                    elif subv16 == 7:
                                        os.system("clear")
                                        while flag:
                                            print(
                                                " Are You Sure Install/Change Version To")
                                            print("1.16.0 Version???")
                                            yn1833 = input("[yes] or [no]: ")
                                            if yn1833 == "yes":
                                                flag = False
                                                os.system("clear")
                                                print("wait....")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["1-16-0"]["url"]
                                                    filenamed = data["minecraft-bedrock-server"]["1-16-0"]["namefile"]
                                                    linxurl = urll.replace(
                                                        "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading assest....")
                                                        urllib.request.urlretrieve(
                                                            linxurl, filenamed)
                                                        print(
                                                            "download success")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                        folname = filenamed.replace(
                                                            ".zip", " ")
                                                    time.sleep(5)
                                                    print("extracting....")
                                                    if os.path.exists("bedrock"):
                                                        print(
                                                            "deleting previous file")
                                                        shutil.rmtree(
                                                            "bedrock")
                                                    if not os.path.exists("bedrock"):
                                                        os.makedirs("bedrock")
                                                    with zipfile.ZipFile(filenamed, "r") as zip_ref:
                                                        zip_ref.extractall(
                                                            "bedrock")
                                                        os.remove(filenamed)
                                                    print("extracting success")
                                                    time.sleep(5)
                                                    svrip = socket.gethostbyname(
                                                        socket.gethostname())
                                                    print("Running...")
                                                    print(
                                                        f"Running in ip: {svrip}")
                                                    time.sleep(5)
                                                    os.system("clear")
                                                    envs = {
                                                        "LD_LIBRARY_PATH": "."}
                                                    subprocess.run(
                                                        ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                                    subprocess.run(
                                                        ["cd bedrock && ./bedrock_server"], env=envs, shell=True)
                                            elif yn1833 == "no":
                                                os.system("clear")
                                                break
                                            else:

                                                print("invalid input")
                                    elif subv16 == 0:
                                        os.system("clear")
                                        break
                                        print("back to previous menu")
                                    else:
                                        os.system(" clear")
                                        print("invalid input")
                                else:
                                    os.system("clear")
                                    print(" input must be number")
                        elif subver == 9:

                            os.system("clear")
                            if not os.path.exists("bedrock"):
                                os.system("clear")
                                print("install server first!!")
                                print("exiting in 10s.....")
                                time.sleep(10)
                                os.system("clear")
                                break
                            elif not os.path.exists(os.path.join("bedrock", "bedrock_server")):
                                os.system("clear")
                                print("file bedrock_server not found!!")
                                print("exiting in 10s....")
                                time.sleep(10)
                                os.system("clear")
                                break
                            elif not os.path.exists(os.path.join("bedrock", "server.properties")):
                                print("file server.properties not found!!!")
                                print("exiting in 10s....")
                                time.sleep(10)
                                os.system("clear")
                                break
                            else:
                                flag = False
                                envs9 = {"LD_LIBRARY_PATH": "."}
                                subprocess.run(
                                    ["chmod +x ./bedrock/bedrock_server"], shell=True)
                                subprocess.run(
                                    ["cd bedrock && ./bedrock_server"], env=envs9, shell=True)
                        elif subver == 11:
                            os.system("clear")
                            while flag:
                                print("[choosen one option]")
                                print("[1] install ngrok")
                                print("[2] run ngrok (run this in another tab)")
                                print("[0] back")
                                toolinput = input(" ")
                                if toolinput.isdigit():
                                        toolinput = int(toolinput)
                                        if toolinput == 1:
                                                os.system("clear")
                                                #flag = False
                                                if os.path.exists("ngrok"):
                                                        print("you have installed ngrok")
                                                print("prepared to download ngrok file...")
                                                time.sleep(5)
                                                with open('data-data.json', 'r') as file:
                                                    data = json.load(file)
                                                    urll = data["minecraft-bedrock-server"]["ngrok"]["url"]
                                                    token = data["ngrok-token"]
                                                    #filenamed = data["minecraft-bedrock-server"]["ngrok"]["namefile"]
                                                    #linxurl = urll.replace(
                                                     #   "bin-win", "bin-linux")

                                                    try:
                                                        print(
                                                            "downloading ngrok file....")
                                                        urllib.request.urlretrieve(
                                                            urll, "ngrok.tgz")
                                                        print(
                                                            "download success")
                                                        os.remove("ngrok.tgz")
                                                    except Exception as e:
                                                        print(f"err: {str(e)}")
                                                    with tarfile.open("ngrok.tgz", 'r:gz') as tar:
                                                       print("extracting ngrok file [ngrok.tgz]")
                                                       tar.extractall()
                                                       print("extract sucess")
                                                    time.sleep(5)
                                                    print("wait for a second....")
                                                    time.sleep(5)
                                                    subprocess.run(["chmod +x ngrok"], shell=True)
                                                    
                                                    subprocess.run([f"./ngrok authtoken {token}"], shell=True)
                                                    #envsn = {"LD_LIBRARY_PATH": "."}
                                                    time.sleep(2)
                                                    os.system("clear")
                                                    print("installing success")
                                                    print("after installing ngrok you can run ngrok script")
                                                    time.sleep(2)
                                                    os.system("clear")
                                        elif toolinput == 2:
                                                os.system("clear")
                                                print("running ngrok....")
                                                if not os.path.exists("ngrok"):
                                                        print("you must installing ngrok first")
                                                with open("data-data.json", "r") as file:
                                                   ttoken = json.load(file)
                                                   tokem = ttoken["ngrok-token"]
                                                   subprocess.run(["chmod +x ngrok"], shell=True)
                                                   subprocess.run(["./ngrok tcp --region=ap 19132"], shell=True)
                                        elif toolinput == 0:
                                                os.system("clear")
                                                break
                                        else:
                                                os.system("clear")
                                else:
                                        os.system("clear")
                        elif subver == 0:
                            os.system("clear")
                            print("back")
                            break
                        else:
                            os.system("clear")
                            print("you must entered a valid selection")
                    else:
                        os.system("clear")
                        print("input must be number")

            elif pilihan == 2:
                os.system("clear")
                print("SORRY MINECRAFT JAVA SERVER NOT AVAILABLE NOW")
            elif pilihan == 3:
                print("exit")
                break
                sys.exit(0)
            else:
                os.system("clear")
                print("Your choice is invalid")
        else:
            os.system("clear")
            print("You must enter a number")
