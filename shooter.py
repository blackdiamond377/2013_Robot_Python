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
		self.lift_button = config.lift_button

		LOADER_COUNT = config.LOADER_COUNT
		BACK_COUNT = config.BACK_COUNT
		FRONT_COUNT = config.FRONT_COUNT
		TOWER_COUNT = config.TOWER_COUNT

		LOADER_SPEED = config.LOADER_SPEED
		BACK_SPEED = config.BACK_SPEED
		FRONT_SPEED = config.FRONT_SPEED
		TOWER_SPEED = config.TOWER_SPEED

		p_manual_shooter_speed = None
		pot_val = None

		self.ss_up_button = config.ss_up_button
		self.ss_down_button = config.ss_down_button
		self.ss_up_pressed = False
		self.ss_down_pressed = False

		self.shooting = False
		self.trigger_time = -1

		self.shooter_piston = config.shooter_piston
		self.extend = config.extend
		self.retract = config.retract

	def op_init(self):
		self.shooter_hall.SetMaxPeriod(1)
		self.shooter_hall.Start()

		self.lift_halls.SetDistancePerPulse(1)
		self.lift_halls.Start()

	def op_tick(self, time):
		lift_speed = self.joy.GetY()
	   # Manual shooter speed adjustments
	    if self.pot_val != ((self.joy.getX() * -1) + 1) / 2:
            manual_shooter_speed = ((self.joy.getX() * -1) + 1) / 2    
        else:
           # if shooter potentiometer hasnt changed then keep the old value including button adjustments
            manual_shooter_speed = self.p_manual_shooter_speed;

        if self.ss_up_button.get() and not ss_up_pressed:
            manual_shooter_speed += .05;
            self.ss_up_pressed = True;
        else:
        	self.ss_up_pressed = False
        
		if self.ss_down_button.get() and not ss_down_pressed:
            manual_shooter_speed -= .05;
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
            if not self.bottomLimit.Get() and lift_speed < 0):
                self.lift.Set(0)
            elif not self.topLimit.Get() and lift_speed > 0:
                self.lift.Set(0)
            elif self.lift_button.get():
                self.lift.Set(lift_speed)
            elif not self.lift_button.get():
                self.lift.Set(0)
            self.shooter.Set(manual_shooter_speed)

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

		shoot(time)
		self.pot_val = ((self.joy.GetX() * -1) + 1) / 2
		self.p_manual_shooter_speed = manual_shooter_speed


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

    def shoot(self, timestamp):
       # If the button is pressed and you aren't yet shooting
        if shoot_button.get() and not self.shooting:
            self.shooting = true
            triggerTime = timestamp
            self.shooter_piston.Set(self.extend)
       # Else, reset and say you aren't shooting anymore
        else:
            currentTime = timestamp
            timeSinceTrigger = currentTime - self.triggerTime
            
            if timeSinceTrigger > 0.6:
                self.shooting = false
            elif timeSinceTrigger > 0.5:
                self.shooter_piston.Set(self.retract)
