import urllib2, json, urllib

token = ''

protocol = 'https' 
api_url = 'api.hipchat.com'

room_url = 'https://api.hipchat.com/v2/room/2489868'

full_url = protocol + '://' + api_url

def send_message(message):
    request = urllib2.Request(room_url+'/notification')
    request.add_header('Authorization', 'Bearer ' + token)
    data = {'message':message, 'color':'yellow'}
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

#print get_room('Random')
mess = ''
while mess != 'quit':
    mess = raw_input('message:')
    send_message(mess)
