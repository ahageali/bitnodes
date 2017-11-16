from ConfigParser import ConfigParser
from pymongo import MongoClient

def get_conf():
  conf = ConfigParser()
  conf.read('conf/mongo.conf')
  parsed = {}
  parsed['ip'] = conf.get('mongo', 'ip')
  parsed['port'] = conf.getint('mongo', 'port')
  parsed['db'] = conf.get('mongo', 'db')
  return parsed

def get_db():
  conf = get_conf()
  client = MongoClient(conf['ip'], conf['port'])
  return client[conf['db']]

