#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import os
redis = redis.Redis('localhost')
id = input("Enter Tabchi Number(1,2,3,...) : ")
sudo = input("Enter Sudo ID : ")
source = os.popen("cat base.lua").read()
launcher = """while true; do
  ./telegram-cli-1222 -p tabchi-{} -s tabchi-{}.lua
done""".format(id,id)
source2 = source.replace("TABCHI-ID",str(id))
newsource = open("tabchi-{}.lua".format(id),"w")
newsource.write(source2)
newsource.close()
newlauncher = open("tabchi-{}.sh".format(id),"w")
newlauncher.write(launcher)
newlauncher.close()
os.popen("chmod 777 tabchi-{}.sh".format(id))
redis.set("tabchi:{}:fullsudo".format(id),sudo)
print("Done!\nNew Tabchi Created...\nID : {}\nSudo : {}\nRun : ./tabchi-{}.sh".format(id,sudo,id))
print('Ch: @BanG_TeaM >> join us')
