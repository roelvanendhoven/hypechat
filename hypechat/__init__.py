import urllib2, json, urllib, sys, getopt
from configwriter import ConfigWriter


#Read initial arguments
try:
    opts, args = getopt.getopt(sys.argv[1:],"hrd:",["help","reset"])
except getopt.GetoptError:
    print 'Error in arguments, see -h or --help for information'
    sys.exit(2)
config = ConfigWriter()


#Sends a message to the chat
def send_message(message,color):   
    request = urllib2.Request(room_url+'/notification')
    request.add_header('Authorization', 'Bearer ' + token)
    data = {'message' : message, 'color': color,'message_format': 'text','notify': True}
    request.add_data(urllib.urlencode(data))
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        print e.read()


def get_rooms():
    request = urllib2.Request(url=full_url+'/v2/room')
    request.add_header('Authorization', 'Bearer ' + token)
    response = urllib2.urlopen(request)
    return json.loads( response.read() )['items']


def get_room(name):
    for room in get_rooms():
        if room['name'] == name:
            return room


def usage():
    print "Commands:"
    print "-h, -help: Display this message"
    print "-r --reset: Reset user settings"
    print "-d: Delete a specific user setting"
    print "An example would be: -d Oauth2token, to delete the token "
    sys.exit()


#checks the inital arguments                                                                    
try:
    opts, args = getopt.getopt(sys.argv[1:],"hrd:",["help","reset"])                           
except getopt.GetoptError:                                                                   
    usage()
    sys.exit(2)                                                                              

#ConfigWriter object
config = ConfigWriter()

for opt, arg in opts:
    if opt in ('-h','--help'):
        usage()
        sys.exit()
    elif opt in ('-r','reset'):
        config.reset()
    elif opt in ('-d','--delete'):
        config.remove(arg)

if config.has("Oauth2token"):
    token = config.get("Oauth2token")
else:
    token = raw_input("OAut2htoken:")
    config.set("Oauth2token", token)

if config.has("Roomkey"):
    roomkey = config.get("Roomkey")
else:
    roomkey = raw_input("Roomkey:")
    config.set("Roomkey",roomkey)

protocol = 'https' 
api_url = 'api.hipchat.com'

print config
room_url = 'https://api.hipchat.com/v2/room/'+roomkey

full_url = protocol + '://' + api_url

#print get_room('Random')
mess = ''
color = raw_input('choose your color:')
while mess != 'quit':
    mess = raw_input('message:')
    send_message(mess,color)
