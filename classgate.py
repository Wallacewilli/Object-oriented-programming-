class Gadget:
    def start(self):
        print("Gadget starting")
class smartphone(Gadget):
    def start(self):
            print("phone is   starting ")
class laptop(Gadget):
    def start(self):
            print("laptop is starting ")

#calling aray of gates 
gadgets=[smartphone(),laptop()]
for gagdet in gadgets:
     gagdet.start()


#next level connect more than two general classes
class Camera:
     def take_photo(self):
          print("camera is taking photo")
class Wifieanble :
     def connect_wifi(self):
          print("connecting to wifi")
class Phone(Gadget,Wifieanble,Camera):
     def start(self):
          print("phone is starting")

#printer
class Smartprinter(Gadget,Wifieanble):
     def start(self):
          print("smart printer is starting")
#use of instance 
devices=[Phone(),Smartprinter()]
for device in devices:
     device.start()
     if isinstance(device,Camera):
          device.take_photo()
     if isinstance(device,Wifieanble):
          device.connect_wifi()
     