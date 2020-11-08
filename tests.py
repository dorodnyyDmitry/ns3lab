import os
import random

log_file = open("logg.txt", "w")

os.chdir("dce/source/ns-3-dce/")

for i in range(2, 21, 2):
  log_file.write("\nTest " + str(i/2) + "\nWindow size: " + str(i*4) + "KB\nDelay: " + str(random.randint(1, 10)*50) + "ms\n")

  os.system("./waf --run \"dce-iperf " + str(i*4) + "KB " + str(random.randint(1, 10)*50)  + "ms\"")

  a = os.popen("cat files-1/var/log/*/*").read()
  log_file.write(a)

log_file.close()

os.chdir("../../../")
