import json, os, logging

class ConfigWriter(object):

    def __init__(self):
        FORMAT = '%(asctime)-15s %(message)s'
        logging.basicConfig(format=FORMAT)
        self.logger = logging.getLogger('configwriter')
        self.logger.setLevel(logging.NOTSET)
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
            try:
                os.makedirs(self.default_path)
            except OSError:
                self.logger.info('Config directory already exists')
            conf = {}
        return conf
    
    def add_key(self,key,value):
        self.config[key] = value
        self.write()
        
    def get(self,key):
        if key in self.config:
            return self.config[key]

    def has(self,key):
        return key in self.config

    def write(self):
        with open(self.default_path + '/' +  self.config_name,'w+') as f:
            self.logger.debug('Config written to file')
            f.write(json.dumps(self.config))


