'''Module with abstract base class (Client) and different Client implementations

'''

import RPi.GPIO as GPIO
from datetime import datetime


class Client(object):
    '''Abstract base class implement to consume & handle message

    '''

    def __init__(self):
        pass

    def handle_message(self, msg):
        '''Handle incoming message specific to your client

        '''
        pass



class GPIOClient(Client):
    '''Raspberry Pi GPIO implementation for Client

    '''

    def __init__(self, *args, **kwargs):
        '''Initialize Class

        '''
        super(GPIOClient, self).__init__(*args, **kwargs)

        self.time = datetime.now()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(18, GPIO.OUT)

        self.whats = ['on', 'off']
        self.devices = ['braai-light', 'man-cave-heater']
    
    def handle_message(self, msg):
        '''Parse the message and decide what to do with it

        # Args:
            msg: incoming message from Slack (string)
        '''
        
        # Set some defaults
        what = self.whats[0]
        device = self.devices[0]

        tokens = msg.split()

        for token in tokens:
            if token in self.whats:
                what = token
            if token in self.devices:
                device = token
        
        # Now action the message
        if device == 'braai-light':
            if what == 'on':
                GPIO.output(18, GPIO.HIGH)
            elif what == 'off':
                GPIO.output(18, GPIO.LOW)


        
class MockClient(Client):
    '''Used to test on non Raspberry Pi devices

    '''
    def __init__(self):
        pass
    
    def handle_message(self, msg):
        whats = ['on', 'off']
        devices = ['braai-light', 'man-cave-heater']
        
        what = whats[0]
        device = devices[0]

        tokens = msg.split()

        for token in tokens:
            if token in whats:
                what = token
            if token in devices:
                device = token
        
        print('I will switch your {} {} for you'.format(device, what))
