class AutomationClient:
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

        