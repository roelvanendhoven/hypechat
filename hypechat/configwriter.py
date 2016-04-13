import json, os, logging

class ConfigWriter(object):

    def __init__(self):
        FORMAT = '%(asctime)-15s %(message)s'
        logging.basicConfig(format=FORMAT)
        self.logger = logging.getLogger('configwriter')
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.FileHandler('log'))
        self.default_path = os.path.expanduser('~') + '/.hypechat'
        self.config_name = 'config.json'
        self.config = self.read(self.default_path + '/' + self.config_name)

    def read(self,path):
        try:
            conf = json.loads(open(path).read())
            self.logger.debug('Config loaded')
        except IOError:
            self.logger.info('Config not found, resorting to backup')
            #os.makedirs(self.config_location)
            conf = {}
        return conf
    
    def add_key(self,key,value):
        self.config[key] = value
        self.write()
        
    def write(self):
        with open(self.default_path + '/' +  self.config_name,'w+') as f:
            self.logger.debug('Config written to file')
            f.write(json.dumps(self.config))


writer = ConfigWriter().add_key('meme','nice')
