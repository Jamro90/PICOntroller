from inputs import get_gamepad, devices

class Devices:
    def __init__(self):
        self.list_of_devs = devices.gamepads
        for dev in self.list_of_devs:
            print(dev)


class Pad(Devices):
    def __init__(self):
        try:
            self.pad = get_gamepad(list_of_devs)
            
        except:
            print("No controller available")
    
    def pad_axis_ret(self):
        while 1:
            for i in self.pad:
                if(i.code == "ABS_X"):
                    print(i.code, i.state)
                elif(i.code == "ABS_Y"):
                    print(i.code, i.state)
                elif(i.code == "ABS_Z"):
                    print(i.code, i.state)
                else:
                    pass


def pad_start():
    print("pad działa")


