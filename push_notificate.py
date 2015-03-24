#coding:utf-8

from pushbullet import Pushbullet
import json
import os

def push():

  # load config file
  config = None
  with open('./config.json') as f:
    config = json.load(f)

  # pushbullet
  pb = Pushbullet(config['access_token'])

  target = None
  for dev in pb.devices:
    if dev.nickname == config['device_name']:
      target = dev

  if target == None:
    print 'target device not found.'
  else:
    
    # push as file
    if config['send_file']:
      if os.path.exists(config['send_file']):
        file_data = None
        try:
          with open(config['send_file'], 'rb') as f:
            file_data = pb.upload_file(f, os.path.basename(config['send_file']))
        except:
          pass
        target.push_file(**file_data)
        print 'pushed as file : {0}'.format(config['send_file'])
        return

    # push as text
    target.push_note(config['send_title'], config['send_body'])
    print 'pushed as text : {0} / {1}'.format(config['send_title'], config['send_body'])

if __name__ == '__main__':
  push()

