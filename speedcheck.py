#!/usr/bin/python3
from speedtest import Speedtest

test = Speedtest()
serv = test.get_best_server()
print("Best server: ",serv["host"])

download = test.download()/1000000
upload = test.upload()/1000000
ping = test.results.ping

print("Download speed is: {:.2f}".format(download))
print("Upload speed is: {:.2f}".format(upload))
print("Ping: {}".format(ping))
