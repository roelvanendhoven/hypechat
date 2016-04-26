# hypechat

Python CLI wrapper for Hipchat v2 API

## Usage

Run with -h to display help, -r to reset the config file.  
Information is stored in ~/.hypechat/config.json right now.

Needed information to run: 
 
* Oauth2token: Generated on the hipchat site
* RoomKey: Should be visible in the browser

This information is stored in the config file. If the information is not found in the config file it will be requested form the user.

color: color to give to your message. Accepted values are:

* yellow
* green
* red
* purple
* gray
* random

This information is not stored.

message: the message that is send to the hipchat room.





