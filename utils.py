import common

class Button(object):

    def __init__(self, joystick, buttonNumber):
        self.joy = joystick
        self.button = buttonNumber

    def get(self):
        return self.joy.GetRawButton(self.button)


class ButtonControlledMotor(common.ComponentBase):

    def __init__(self, config):
        self.motor = config.motor
        self.up_button = config.up_button
        self.down_button = config.down_button

    def op_init(self):
        self.motor.Set(0)

    def op_tick(self, time):
        if self.up_button.get():
            if self.down_button.get():
                self.motor.Set(0)
            else:
                self.motor.Set(-1)
        elif self.down_button.get():
            self.motor.Set(1)
        else:
            self.motor.Set(0)


class CounterPIDSource(object):
    
    def __init__(self, counter, buffer):
        self.counter = counter
        self.speeds = buffer

    def get_buffered_rpm(self):
        return self.PID_get()

    def get_rps(self):
        return 1/self.counter.GetPeriod()

    def PID_get(self):
        self.speeds.add(self.get_rpm())
        return self.speeds.get_average()

    def get_rpm():
        return self.get_rps()*60



class RingBuffer(object):

    def __init__(self, length):
        self.length = length
        buffer = []
        self.idx = 0

    def add(newVal):
        self.buffer[idx] = newVal
        self.idx++
        if self.idx > self.length:
            self.idx = 0

    def get_average(self):
        total = 0
        for i in range(self.length):
            total += self.buffer[i]
        return total / self.length
