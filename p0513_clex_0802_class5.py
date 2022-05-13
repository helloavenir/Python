class Television :
    def __init__(self, channel, volume, on) :
        self.channel = channel
        self.volume = volume
        self.on = on

    def show(self) :
        print(self.channel, self.volume, self.on)

    def set_channel(self, channel) :
        set_channel = channel

    def get_channel(self) :
        return self.channel

t = Television(5, 10, True)
t.show()
print(t.get_channel())

t.set_channel(10)
t.show()





    
