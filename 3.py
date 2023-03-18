import os, socket

cur_dir = os.getcwd()
path = cur_dir+"/ip.log"

urls = {
    "drive.google.com": None,
    "mail.google.com": None,
    "google.com": None
}

for u in urls:
    ip = socket.gethostbyname(u)
    urls[u] = ip
    print(f"IP адрес для сервиса {u}: {ip}")


if not os.path.isfile(path):
    with open(path,"w") as file:
        for u in urls:
            file.write(f"{urls[u]}\n{u}\n")
    file.close()
else:
    with open(path, "r+") as file:
        old_ips = file.read().splitlines()

        for u in urls:
            if urls[u] not in old_ips:
                print(f"[ERROR] {u} IP mismatch: {urls[u]} {old_ips[old_ips.index(u)-1]}")

        file.seek(0)
        file.truncate(0)

        for u in urls:
            file.write(f"{urls[u]}\n{u}\n")
    file.close()