from math import sin,cos,radians,pi

class automission(object):
	#docstring for automission
	def __init__(self,vehicle_type):

		super(automission, self).__init__()
		assert vehicle_type=='copter'
		self.mlist=[] #each element of the array represents a command, ie waypoint, with its parameters
		self.counter=1

		#these two lines are by default, exists every mission planner file
		self.mlist.append('QGC WPL 110\n')
		self.mlist.append('0	1	0	0	0	0	0	0	0	0	0	1\n') 


	def param_to_mcommand(self,*args): #takes command and its parameters, appends them
					 #to mlist while adjusting formatting

		string=str(self.counter)+'	'
		self.counter+=1

		for i in args:	
			string+=str(i)+'	'
		string+='\n'	

		self.mlist.append(string)


### Mission Commands ###

# detailed information about commands and their functionality
# visit  http://copter.ardupilot.com/wiki/mission-command-list/#land

	################################################################################
	
	#every parameter list begins with '0,3,' and ends with ',1'
	
	def waypoint(self,lat,lon,alt,delay=0):	
		waypoint_id=16
		self.param_to_mcommand(0,3,waypoint_id,delay,0,0,0,lat,lon,alt,1)
		
	def takeoff(self,angle,alt,lat=0,lon=0):
		takeoff_id=22
		self.param_to_mcommand(0,3,takeoff_id,angle,0,0,0,lat,lon,alt,1)

	def land(self,lat=0,lon=0,alt=0):
		landid=21
		self.param_to_mcommand(0,3,landid,0,0,0,0,lat,lon,alt,1)

	def loiter_unlim(self,lat,lon,alt):	
		loiter_unlimid=17
		self.param_to_mcommand(0,3,loiter_unlimid,0,0,0,0,lat,lon,alt,1)
	
	def do_set_roi(self,lat,lon,alt=0):	
		do_set_roi_id=201
		self.param_to_mcommand(0,3,do_set_roi_id,0,0,0,0,lat,lon,alt,1)

	def rtl(self):	
		rtl_id=20
		self.param_to_mcommand(0,3,rtl_id,0,0,0,0,0,0,0,1)

	def spline_waypoint(self,lat,lon,alt,delay=0):
		spline_waypoint_id=82
		self.param_to_mcommand(0,3,spline_waypoint_id,delay,0,0,0,lat,lon,alt,1)

	def loiter_time(self,time,lat=0,lon=0,alt=0):
		loiter_time_id=19
		self.param_to_mcommand(0,3,loiter_time_id,time,0,0,0,lat,lon,alt,1)
	
	def loiter_turns(self,turn,direction,lat=0,lon=0,alt=0):
		loiter_turns_id=18
		self.param_to_mcommand(0,3,loiter_turns_id,turn,0,direction,0,lat,lon,alt,1)

	def loiter_unlim(self,lat=0,lon=0,alt=0):
		loiter_unlim_id=17
		self.param_to_mcommand(0,3,loiter_unlim_id,0,0,0,0,lat,lon,alt,1)

	def condition_delay(self,time):
		condition_delay_id=112
		self.param_to_mcommand(0,3,condition_delay_id,time,0,0,0,0,0,0,1)

	def condition_distance(self,dist):
		condition_distance_id=114
		self.param_to_mcommand(0,3,condition_distance_id,dist,0,0,0,0,0,0,1)

	def condition_yaw(self,deg,rel_abs,dir=0):
		condition_yaw_id=115
		self.param_to_mcommand(0,3,condition_yaw_id,deg,0,dir,rel_abs,0,0,0,1)

	def do_jump(self,wp_number,repeat):
		do_jump_id=177
		self.param_to_mcommand(0,3,do_jump_id,wp_number,repeat,0,0,0,0,0,1)

	def do_change_speed(self,speed):
		do_change_speed_id=178
		self.param_to_mcommand(0,3,do_change_speed_id,speed,0,0,0,0,0,0,1)

	def do_set_home(self,current=1,lat=0,lon=0):
		do_set_home_id=179
		self.param_to_mcommand(0,3,do_set_home_id,current,0,0,0,lat,lon,0,1)

	def do_digicam_control(self):
		do_digicam_control_id=203
		self.param_to_mcommand(0,3,do_digicam_control_id,0,0,0,0,0,0,0,1)
		



	####################################################################################


	def write(self,name='output'): 		

	# saves final command list mlist as txt file. 
	# Missionplanner can direcly open this text document in flight plan / load WP file button

			with open(str(name)+".txt", "w") as text_file:
				for i in self.mlist:
					text_file.write(i)


"""
	def meter_to_coord(self,meter,angle,lat,lon):

		m_x=meter*cos(radians(angle))
		m_y=meter*sin(radians(angle))
		R=6378137
		yLat = m_y/R
		xLon = m_x/(R*cos(radians(lat)))
		lat_new= lat + yLat * 180/pi
		lon_new=lon+xLon*180/pi
		return lat_new,lon_new

		"""

