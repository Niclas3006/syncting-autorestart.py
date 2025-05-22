# syncting-autorestart.py
a python script to restart syncthing via the API


# Why does this exist?
I have a server runing syncthing 24/7, but somehow syncthing is filling up some resource limit so I can't use the server for something else, for exaple also host a minecraft server.
It gets realy messy since sometimes no files can be opend anymore, this only happens after a few days of continuously running syncthing, and a simple restart of syncthing frees up the resources again.
So to solve my issues, I made this simple script to restart syncthing every hour to keep ressource uses in check, this is done softly and throug the API of syncthing.
Also if the syncthing server is shut down via the web-interface, then the python script will also terminate, since it won't be needed until syncthing is manually started again.

# Usage
The script requires the following python packages
```
datetime time requests
```

To set it up, paste your syncting api key (you can get it easyly in the web GUI) in the syncthing_api_key variable, 
ensure you point the restart and ping url variable to the right adress.
Restart and ping url should be:
```
restart_url= "http://[YOUR SYNCTHING URL]/rest/system/restart"
ping_url= "http://[YOUR SYNCTHING URL]/rest/system/ping"
```
replace `[YOUR SYNCTHING URL]` with your URL. 

When everything is configured, run the python file
```
python main.py
```

IMPORTANT:
The script is meant to run on the same server and using the internal adress to communicate with syncthing. It is not ensured to work with SSL enabled, so ensure you are using the http adress.



# Credits and links
Script by Niclas3006

Syncthing: https://syncthing.net/
Syncthing API Documentation:  https://docs.syncthing.net/dev/rest.html
