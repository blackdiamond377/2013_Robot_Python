import common


__all__ = ['Shooter']

class Shooter(common.ComponentBase):

	LOADER_COUNT = None
	BACK_COUNT = None
	FRONT_COUNT = None
	TOWER_COUNT = None
	
	LOADER_SPEED = None
	BACK_SPEED = None
	FRONT_SPEED = None
	TOWER_SPEED  = None
	
	def __init__(self, config):
		self.joy = config.shooter_joy
		self.presets = config.presets

		self.shooter_motor = config.shooter_motor
		self.shooter_hall = config.shooter_hall

		self.hall_source = config.hall_source
		self.top_hall = config.top_hall
		self.bottom_hall = config.bottom_hall

		self.lift_halls = config.lift_halls
		self.lift = config.lift

		LOADER_COUNT = config.LOADER_COUNT
		BACK_COUNT = config.BACK_COUNT
		FRONT_COUNT = config.FRONT_COUNT
		TOWER_COUNT = config.TOWER_COUNT

		LOADER_SPEED = config.LOADER_SPEED
		BACK_SPEED = config.BACK_SPEED
		FRONT_SPEED = config.FRONT_SPEED
		TOWER_SPEED = config.TOWER_SPEED

		self.ss_up_button = config.ss_up_button
		self.ss_down_button = config.ss_down_button
		self.ss_up_pressed = False
		self.ss_down_pressed = False

	def op_init(self):
		self.shooter_hall.SetMaxPeriod(1)
		self.shooter_hall.Start()

		self.lift_halls.SetDistancePerPulse(1)
		self.lift_halls.Start()

	def op_tick(self, time):
		shooterRPM = self.hall_source.get_buffered_rpm()


	   # Manual shooter speed adjustments
	    if shooterPotVal != ((joy1.getX() * -1) + 1) / 2:
            manualShooterSpeed = ((joy1.getX() * -1) + 1) / 2    
        else:
           # if shooter potentiometer hasnt changed then keep the old value including button adjustments
            manualShooterSpeed = previousManualShooterSpeed;

        if self.ss_up_button.get() and not ss_up_pressed:
            manualShooterSpeed += .05;
            self.ss_up_pressed = True;
        else:
        	self.ss_up_pressed = False
        
		if self.ss_down_button.get() and not ss_down_pressed:
            manualShooterSpeed -= .05;
            self.ss_down_pressed = True;
        else:
        	self.ss_down_pressed = False

       # Presets
	    # Zero
		if self.presets[0].get():
			lift_to_count(0)
			self.shooter_motor.Set(0)
	    # Loading
		elif self.presets[1].get():
			lift_to_count(LOADER_COUNT)
			self.shooter_motor.Set(LOADER_SPEED)
	    # Manual
		elif self.presets[2].get():
            if not bottomLimit.Get() and liftSpeed < 0):
                lift.Set(0)
            elif not topLimit.Get() and liftSpeed > 0:
                lift.Set(0)
            elif joy1.getRawButton(2):
                lift.Set(liftSpeed)
            elif not joy1.getRawButton(2)):
                lift.Set(0)
            shooter.set(manualShooterSpeed)

	    # Back
		elif self.presets[3].get():
			lift_to_count(BACK_COUNT)
			self.shooter_motor.Set(BACK_SPEED)
	    # Front
	   	elif self.presets[4].get():
	   		lift_to_count(FRONT_COUNT)
			self.shooter_motor.Set(FRONT_SPEED)
	    # Tower
	    elif self.presets[5].get():
	    	lift_to_count(TOWER_COUNT)
			self.shooter_motor.Set(TOWER_SPEED)


	def lift_to_count(self, destination):
        count = float(lift_halls.GetRaw())
        
        if count != destination :
            speed = -((destination - count) / 200
            
           # Keeps motor moving when close
            if speed < 0:
                speed -= .2
            else:
                speed += .2
           
           # Sets the lift speed as long as it hasn't hit a limit 
            if speed < 0 and self.bottom_limit.Get():
            	self.lift.Set(speed)
            elif speed > 0 and self.top_limit.Get()
                self.lift.Set(speed)
            else:
                self.lift.Set(0)

        else:
            self.lift.Set(0)
    